from pymongo import MongoClient
from pymongo.errors import PyMongoError
from typing import Any, Dict, List


class CRUD:
    """
    CRUD helper class for MongoDB.
    Provides Create, Read, Update, and Delete operations.
    """

    def __init__(self, username: str, password: str, db_name: str = "aac",
                 host: str = "localhost", port: int = 27017, authSource: str = "admin"):
        """
        Initialize the MongoDB client and select the database.
        """
        uri = f"mongodb://{username}:{password}@{host}:{port}/?authSource={authSource}"
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def insert_document(self, collection_name: str, document: Dict[str, Any]) -> bool:
        """
        Insert a single document into the named collection.
        Returns True if insert was acknowledged, False otherwise.
        """
        try:
            if not isinstance(document, dict):
                raise TypeError("document must be a dict")
            coll = self.db[collection_name]
            result = coll.insert_one(document)
            return bool(getattr(result, "acknowledged", False))
        except (PyMongoError, TypeError) as e:
            print(f"[insert_document] Error: {e}")
            return False

    def find_documents(self, collection_name: str, query: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Find documents matching query in the named collection.
        Returns a list of documents (may be empty) or [] on error.
        """
        try:
            coll = self.db[collection_name]
            cursor = coll.find(query)
            results = list(cursor)
            return results
        except PyMongoError as e:
            print(f"[find_documents] Error: {e}")
            return []

    def update_documents(self, collection_name: str, query: Dict[str, Any],
                         new_values: Dict[str, Any], many: bool = False) -> int:
        """
        Update one or more documents matching the query in the named collection.
        Input:
            - query: key/value pair(s) for the document(s) to find
            - new_values: key/value pair(s) to update
            - many: if True, update many; else update one
        Returns the number of documents modified.
        """
        try:
            coll = self.db[collection_name]
            update = {"$set": new_values}
            if many:
                result = coll.update_many(query, update)
            else:
                result = coll.update_one(query, update)
            return result.modified_count
        except PyMongoError as e:
            print(f"[update_documents] Error: {e}")
            return 0

    def delete_documents(self, collection_name: str, query: Dict[str, Any], many: bool = False) -> int:
        """
        Delete one or more documents matching the query in the named collection.
        Input:
            - query: key/value pair(s) for the document(s) to remove
            - many: if True, delete many; else delete one
        Returns the number of documents deleted.
        """
        try:
            coll = self.db[collection_name]
            if many:
                result = coll.delete_many(query)
            else:
                result = coll.delete_one(query)
            return result.deleted_count
        except PyMongoError as e:
            print(f"[delete_documents] Error: {e}")
            return 0
