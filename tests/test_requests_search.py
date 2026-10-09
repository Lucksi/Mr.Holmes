import json
import os
import tempfile
import unittest
from unittest import mock

from Core.Support import Requests_Search as RS
from tests.helpers import fake_response

SITE = {"name": "Demo", "main": "demo.com", "user": "https://demo.com/{}", "user2": "https://demo.com/{}",
        "Error": "Status-Code", "text": "not found", "response": "https://demo.com/404",
        "exception": [" "], "Scrapable": "False", "Tag": ["Social"]}


class DetectTest(unittest.TestCase):

    def test_status_code_rules(self):
        self.assertTrue(RS._detect("Status-Code", SITE, fake_response(200)))
        self.assertFalse(RS._detect("Status-Code", SITE, fake_response(404)))
        self.assertIsNone(RS._detect("Status-Code", SITE, fake_response(403)))
        self.assertIsNone(RS._detect("Status-Code", SITE, fake_response(429)))

    def test_message_rule_ignores_block_pages(self):
        self.assertFalse(RS._detect("Message", SITE, fake_response(200, "user not found here")))
        self.assertTrue(RS._detect("Message", SITE, fake_response(200, "profile page")))
        # A Cloudflare challenge lacks the 'not found' text but must not count as found
        self.assertIsNone(RS._detect("Message", SITE, fake_response(403, "challenge")))

    def test_response_url_rule(self):
        self.assertFalse(RS._detect("Response-Url", SITE, fake_response(200, url="https://demo.com/404/")))
        self.assertTrue(RS._detect("Response-Url", SITE, fake_response(200, url="https://demo.com/alice")))


class SearchTest(unittest.TestCase):

    def setUp(self):
        RS._control_cache.clear()
        self.dir = tempfile.mkdtemp()
        self.report = os.path.join(self.dir, "alice.txt")
        self.json1 = os.path.join(self.dir, "alice.json")
        self.json2 = os.path.join(self.dir, "Name.json")

    def run_search(self, main_response, control_response):
        found, names, scrap, tags, most = [], [], [], [], []
        with mock.patch.object(RS.Http, "get", return_value=control_response):
            RS.Search.search("Status-Code", self.report, "https://demo.com/alice", "https://demo.com/alice",
                             None, {"Demo": SITE}, "Demo", "alice", "USERNAME", found, "Demo", names,
                             "False", scrap, True, "demo.com", self.json1, self.json2, ["Social"], tags, most,
                             response=main_response)
        with open(self.report.replace(".txt", "_data.json")) as f:
            return found, json.load(f)["accounts"][-1]

    def test_positive_confirmed_by_control_probe(self):
        found, record = self.run_search(fake_response(200), fake_response(404))
        self.assertEqual(found, ["https://demo.com/alice"])
        self.assertEqual(record["result"], "found")
        self.assertEqual(record["confidence"], "high")

    def test_false_positive_discarded_when_random_account_also_found(self):
        found, record = self.run_search(fake_response(200), fake_response(200))
        self.assertEqual(found, [])
        self.assertEqual(record["result"], "inconclusive")
        self.assertEqual(record["confidence"], "unreliable-site")

    def test_not_found(self):
        found, record = self.run_search(fake_response(404), fake_response(404))
        self.assertEqual(found, [])
        self.assertEqual(record["result"], "not-found")


if __name__ == "__main__":
    unittest.main()
