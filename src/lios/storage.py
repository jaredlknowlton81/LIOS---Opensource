"""Storage — a minimal, backend-agnostic persistence layer.

Ships with an in-memory backend so the rest of LIOS is fully testable without
a database. A `JSONFileStore` is provided for the lowest-friction real
persistence (e.g. logging Omi wearable reflections to a single JSON file);
swap in something heavier (sqlite, postgres) by implementing the same
`Store` protocol.
"""

from __future__ import annotations

import json
import os
from dataclasses import asdict, is_dataclass
from datetime import datetime
from typing import Any, Protocol


def _default_json(obj: Any) -> Any:
    if isinstance(obj, datetime):
        return obj.isoformat()
    if is_dataclass(obj) and not isinstance(obj, type):
        return asdict(obj)
    if hasattr(obj, "value"):  # Enum
        return obj.value
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


class Store(Protocol):
    def put(self, collection: str, record_id: str, record: Any) -> None: ...
    def get(self, collection: str, record_id: str) -> Any | None: ...
    def all(self, collection: str) -> list[Any]: ...
    def delete(self, collection: str, record_id: str) -> None: ...


class MemoryStore:
    """Simple in-memory implementation of the Store protocol."""

    def __init__(self) -> None:
        self._data: dict[str, dict[str, Any]] = {}

    def put(self, collection: str, record_id: str, record: Any) -> None:
        self._data.setdefault(collection, {})[record_id] = record

    def get(self, collection: str, record_id: str) -> Any | None:
        return self._data.get(collection, {}).get(record_id)

    def all(self, collection: str) -> list[Any]:
        return list(self._data.get(collection, {}).values())

    def delete(self, collection: str, record_id: str) -> None:
        self._data.get(collection, {}).pop(record_id, None)


class JSONFileStore:
    """Append-friendly JSON file backend for low-friction field data capture.

    Not intended for concurrent writers or large datasets — it's the
    lowest-effort way to make Omi-style nightly reflections durable, not a
    production database.
    """

    def __init__(self, path: str) -> None:
        self.path = path
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                json.dump({}, f)

    def _read(self) -> dict[str, dict[str, Any]]:
        with open(self.path, encoding="utf-8") as f:
            return json.load(f)

    def _write(self, data: dict[str, dict[str, Any]]) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, default=_default_json, indent=2)

    def put(self, collection: str, record_id: str, record: Any) -> None:
        data = self._read()
        data.setdefault(collection, {})[record_id] = (
            asdict(record) if is_dataclass(record) and not isinstance(record, type) else record
        )
        self._write(data)

    def get(self, collection: str, record_id: str) -> Any | None:
        return self._read().get(collection, {}).get(record_id)

    def all(self, collection: str) -> list[Any]:
        return list(self._read().get(collection, {}).values())

    def delete(self, collection: str, record_id: str) -> None:
        data = self._read()
        data.get(collection, {}).pop(record_id, None)
        self._write(data)
