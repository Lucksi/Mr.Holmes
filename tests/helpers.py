import requests


def fake_response(status=200, text="", url="https://example.com/", headers=None):
    r = requests.Response()
    r.status_code = status
    r._content = text.encode()
    r.url = url
    r.headers.update(headers or {})
    r.encoding = "utf-8"
    return r
