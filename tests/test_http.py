import unittest
from unittest import mock

import requests

from Core.Support import Http, Proxies
from tests.helpers import fake_response


class HttpTest(unittest.TestCase):

    def test_falls_back_to_direct_connection_when_proxy_fails(self):
        calls = []

        def fake_request(method, url, proxies=None, **kw):
            calls.append(proxies)
            if proxies:
                raise requests.exceptions.ProxyError("proxy down")
            return fake_response(200)

        with mock.patch.object(Http.session(), "request", side_effect=fake_request):
            r = Http.get("https://example.com", proxies={"https": "http://1.2.3.4:8080"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(calls, [{"https": "http://1.2.3.4:8080"}, None])

    def test_get_json_returns_none_on_http_error(self):
        with mock.patch.object(Http, "get", return_value=fake_response(500, "{}")):
            self.assertIsNone(Http.get_json("https://example.com"))

    def test_fetch_many_returns_exceptions_instead_of_raising(self):
        def fake_get(url, **kw):
            if "bad" in url:
                raise requests.exceptions.ConnectionError("down")
            return fake_response(200, url=url)

        with mock.patch.object(Http, "get", side_effect=fake_get):
            out = Http.fetch_many([("a", "https://ok", None), ("b", "https://bad", None)])
        self.assertEqual(out["a"].status_code, 200)
        self.assertIsInstance(out["b"], Exception)

    def test_user_agent_is_never_empty(self):
        self.assertTrue(Http.random_agent())

    def test_proxy_url_has_scheme_and_no_newline(self):
        if Proxies.proxy.final_proxis:
            url = Proxies.proxy.final_proxis["https"]
            self.assertTrue(url.startswith("http://"))
            self.assertNotIn("\n", url)


if __name__ == "__main__":
    unittest.main()
