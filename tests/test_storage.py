import os
import tempfile

from lios.storage import JSONFileStore, MemoryStore


def test_memory_store_put_get_all_delete():
    store = MemoryStore()
    store.put("entities", "e1", {"name": "Greg"})
    assert store.get("entities", "e1") == {"name": "Greg"}
    assert store.all("entities") == [{"name": "Greg"}]
    store.delete("entities", "e1")
    assert store.get("entities", "e1") is None


def test_json_file_store_roundtrip():
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "data.json")
        store = JSONFileStore(path)
        store.put("reflections", "r1", {"question": "What mattered today?", "answer": "Clarity."})
        assert store.get("reflections", "r1")["answer"] == "Clarity."

        # simulate reopening the store later
        store2 = JSONFileStore(path)
        assert store2.get("reflections", "r1")["question"] == "What mattered today?"

        store2.delete("reflections", "r1")
        assert store2.get("reflections", "r1") is None
