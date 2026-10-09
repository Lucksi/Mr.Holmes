import socket
import threading
import unittest
from unittest import mock

from Core.Support.Mail import Domain
from Core.Support.Websites import Recon, Scanner
from tests.helpers import fake_response


class ReconTest(unittest.TestCase):

    def test_normalize_and_ip_detection(self):
        self.assertEqual(Recon.normalize("HTTPS://Example.com:8443/path"), "example.com")
        self.assertTrue(Recon.is_ip("8.8.8.8"))
        self.assertFalse(Recon.is_ip("example.com"))

    def test_ct_subdomains_parsing(self):
        data = [{"name_value": "*.example.com\nwww.example.com"},
                {"name_value": "api.example.com"}, {"name_value": "evil.com"}]
        with mock.patch.object(Recon.Http, "get_json", return_value=data):
            self.assertEqual(Recon.ct_subdomains("example.com"), ["api.example.com", "www.example.com"])
        with mock.patch.object(Recon.Http, "get_json", return_value=None):
            self.assertIsNone(Recon.ct_subdomains("example.com"))

    def test_http_profile_detects_tech_and_missing_headers(self):
        html = '<html><head><title>Hi</title><meta name="generator" content="WordPress 6.5"></head>' \
               '<link href="/wp-content/x.css"></html>'
        response = fake_response(200, html, headers={"Server": "nginx/1.24.0", "CF-Ray": "abc",
                                                     "X-Frame-Options": "DENY"})
        with mock.patch.object(Recon.Http, "get", return_value=response):
            profile = Recon.http_profile("example.com")
        self.assertEqual(profile["title"], "Hi")
        self.assertIn("WordPress", profile["technologies"])
        self.assertIn("Cloudflare", profile["technologies"])
        self.assertIn("X-Frame-Options", profile["security_headers_present"])
        self.assertIn("Strict-Transport-Security", profile["security_headers_missing"])

    def test_rdap_parsing(self):
        data = {"handle": "H1", "status": ["active"], "nameservers": [{"ldhName": "NS1.X.COM"}],
                "events": [{"eventAction": "registration", "eventDate": "2000-01-01"}],
                "entities": [{"roles": ["registrar"], "publicIds": [{"identifier": "292"}],
                              "vcardArray": ["vcard", [["version", {}, "text", "4.0"], ["fn", {}, "text", "MarkMonitor"]]]}]}
        with mock.patch.object(Recon.Http, "get_json", return_value=data):
            info = Recon.rdap("example.com")
        self.assertEqual(info["registrar"], "MarkMonitor")
        self.assertEqual(info["registration"], "2000-01-01")
        self.assertEqual(info["registrar_iana_id"], "292")


class MailDomainTest(unittest.TestCase):

    def test_mail_records(self):
        answers = {("example.com", "MX"): ["20 mx2.example.com.", "10 mx1.example.com."],
                   ("example.com", "TXT"): ['"v=spf1 -all"', '"google-site-verification=x"'],
                   ("_dmarc.example.com", "TXT"): ['"v=DMARC1; p=reject"'],
                   ("_mta-sts.example.com", "TXT"): []}
        with mock.patch.object(Domain.Recon, "dns_query", side_effect=lambda n, t: answers.get((n, t), [])):
            rec = Domain.mail_records("example.com")
        self.assertEqual(rec["mx"][0], "10 mx1.example.com.")
        self.assertEqual(rec["spf"], ["v=spf1 -all"])
        self.assertEqual(rec["dmarc_policy"], "reject")
        self.assertFalse(rec["mta_sts"])
        self.assertTrue(rec["accepts_mail"])

    def test_null_mx_means_no_mail(self):
        with mock.patch.object(Domain.Recon, "dns_query", side_effect=lambda n, t: ["0 ."] if t == "MX" else []):
            self.assertFalse(Domain.mail_records("example.com")["accepts_mail"])


class ScannerTest(unittest.TestCase):

    def test_product_version(self):
        self.assertEqual(Scanner.Port.product_version("SSH-2.0-OpenSSH_8.9p1 Ubuntu"), "OpenSSH 8.9p1")
        self.assertEqual(Scanner.Port.product_version("Apache/2.4.58 (Unix)"), "Apache 2.4.58")
        self.assertIsNone(Scanner.Port.product_version("cloudflare"))

    def test_scan_and_banner_on_local_socket(self):
        server = socket.socket()
        server.bind(("127.0.0.1", 0))
        server.listen(5)
        port = server.getsockname()[1]

        def serve():
            for _ in range(2):
                conn, _ = server.accept()
                conn.sendall(b"SSH-2.0-OpenSSH_9.6\r\n")
                conn.close()

        threading.Thread(target=serve, daemon=True).start()
        self.assertEqual(Scanner.Port.scan_ports("127.0.0.1", [port]), [port])
        self.assertEqual(Scanner.Port.grab_banner("127.0.0.1", port, "localhost"), "SSH-2.0-OpenSSH_9.6")
        server.close()

    def test_known_cves_parsing(self):
        data = {"vulnerabilities": [{"cve": {"id": "CVE-2024-6387", "descriptions": [{"lang": "en", "value": "race"}],
                                             "metrics": {"cvssMetricV31": [{"cvssData": {"baseScore": 8.1}}]}}}]}
        with mock.patch.object(Scanner.Http, "get_json", return_value=data):
            self.assertEqual(Scanner.Port.known_cves("OpenSSH 9.6"),
                             [{"id": "CVE-2024-6387", "cvss": 8.1, "summary": "race"}])


if __name__ == "__main__":
    unittest.main()
