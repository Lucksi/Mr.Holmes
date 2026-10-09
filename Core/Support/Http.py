# Shared HTTP layer: one pooled session per thread, automatic retries with
# backoff, split connect/read timeouts, User-Agent rotation and transparent
# fallback to a direct connection when the configured proxy fails.

import random
import threading
from concurrent.futures import ThreadPoolExecutor

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from Core.Support import Useragent

TIMEOUT = (6, 15)
WORKERS = 16
_local = threading.local()
_PROXY_ERRORS = (requests.exceptions.ProxyError,
                 requests.exceptions.ConnectionError,
                 requests.exceptions.Timeout)


def random_agent():
    agents = [a.strip() for a in Useragent.Select.value if a.strip()]
    return random.choice(agents) if agents else Useragent.DEFAULT_AGENT


def session():
    s = getattr(_local, "session", None)
    if s is None:
        retry = Retry(total=3, connect=3, read=2, status=3, backoff_factor=0.8,
                      status_forcelist=(429, 500, 502, 503, 504),
                      allowed_methods=frozenset(["GET", "HEAD", "POST"]),
                      respect_retry_after_header=True, raise_on_status=False)
        adapter = HTTPAdapter(max_retries=retry, pool_connections=WORKERS, pool_maxsize=WORKERS)
        s = requests.Session()
        s.mount("http://", adapter)
        s.mount("https://", adapter)
        _local.session = s
    return s


def _headers(extra):
    h = {"User-Agent": random_agent(),
         "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
         "Accept-Language": "en-US,en;q=0.8"}
    if extra:
        h.update(extra)
    return h


def request(method, url, proxies=None, headers=None, timeout=TIMEOUT, fallback=True, **kw):
    h = _headers(headers)
    try:
        return session().request(method, url, headers=h, proxies=proxies, timeout=timeout, **kw)
    except _PROXY_ERRORS:
        if proxies and fallback:
            return session().request(method, url, headers=h, proxies=None, timeout=timeout, **kw)
        raise


def get(url, **kw):
    return request("GET", url, **kw)


def post(url, **kw):
    return request("POST", url, **kw)


def get_json(url, **kw):
    """Return parsed JSON, or None on network/HTTP/decoding errors."""
    try:
        r = get(url, **kw)
        if r.status_code >= 400:
            return None
        return r.json()
    except (requests.exceptions.RequestException, ValueError):
        return None


def fetch_many(jobs, proxies=None, workers=WORKERS, **kw):
    """jobs: iterable of (key, url, headers). Returns {key: Response | Exception}."""
    jobs = list(jobs)

    def one(job):
        key, url, headers = job
        try:
            return key, get(url, proxies=proxies, headers=headers, **kw)
        except Exception as e:
            return key, e

    with ThreadPoolExecutor(max_workers=max(1, min(workers, len(jobs) or 1))) as pool:
        return dict(pool.map(one, jobs))
