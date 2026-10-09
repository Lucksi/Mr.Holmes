# Structured JSON output that lives next to each text report
# (report.txt -> report_data.json), so results can be parsed or exported.

import json
import os
import threading
from datetime import datetime, timezone

_lock = threading.Lock()


def path_for(report):
    return os.path.splitext(report)[0] + "_data.json"


def _load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def _dump(path, data):
    data["_generated"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4, default=str)


def save(report, section, payload):
    path = path_for(report)
    with _lock:
        data = _load(path)
        data[section] = payload
        _dump(path, data)


def append(report, section, item):
    path = path_for(report)
    with _lock:
        data = _load(path)
        data.setdefault(section, []).append(item)
        _dump(path, data)
