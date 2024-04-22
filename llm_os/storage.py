"""RAG for storage of data in the LLM OS."""
from typing import List, Dict
import chromadb  # type: ignore
from llm_os import ROOT_DIR

storage_path = (ROOT_DIR / "db").resolve()
client = chromadb.PersistentClient(path=str(storage_path))

collection_name = "storage_collection"
collection = client.get_or_create_collection(
    collection_name, metadata={"hnsw:space": "cosine"}
)


def upsert_data(
    documents: List[str] | str,
    metadata: List[Dict[str, str]] | Dict[str, str],
    ids=List[str] | str,
):
    # if they're strings, convert to lists
    if isinstance(documents, str):
        documents = [documents]

    if isinstance(metadata, str):
        metadata = [metadata]

    if isinstance(ids, str):
        ids = [ids]

    collection.add(documents, metadata, ids)


def query_db(query: str, top_k: int = 10):
    return collection.query([query], n_results=top_k)
