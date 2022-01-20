import copy
import logging
from datetime import datetime

from bson import ObjectId

logger = logging.getLogger(__name__)


class AmzManager:

    COLLECTION_NAME = "amz"

    @classmethod
    def validate_collection_name(cls):
        """Validate exists collection name"""
        if not cls.COLLECTION_NAME:
            raise "EMPTY COLLECTION"

    @classmethod
    def get_collection(cls):
        """Get Collection"""
        from main import db
        cls.validate_collection_name()
        return db.get_collection(cls.COLLECTION_NAME)

    @classmethod
    def get_by_id(cls, value_id: str):
        """Get single objects
        params:
            value_id(str): Value ID
        """
        collection = cls.get_collection()
        try:
            value = collection.find_one(
                {'_id': ObjectId(value_id)}
            )

        except Exception:
            raise "Value Dont Exists"

        # In case of being an empty value,
        # we execute a raise error,
        # I say that the value does not exist
        if not value:
            raise "Value Dont Exists"
        return value

    @classmethod
    def filter_values(cls, query: dict = None):
        """Filter values by query
        """
        collection = cls.get_collection()
        data_query = copy.deepcopy(query) or {}
        try:
            values = collection.find(data_query)
        except Exception:
            values = []

        return values

    @classmethod
    def insert_one(cls, data: dict = None):
        """Insert single value
        params:
            data(dict): Data to create document.
        """
        data_insert = copy.deepcopy(data) or {}
        now = datetime.today()
        if data_insert:
            data_insert["create_date"] = now
            data_insert["last_modified"] = now
        collection = cls.get_collection()
        try:
            value = collection.insert_one(data_insert)
        except Exception as error:
            raise str(error)

        return value

    @classmethod
    def remove(cls, query: str = None):
        """Remove data from collection"""
        collection = cls.get_collection()
        data_insert = copy.deepcopy(query) or {}
        try:
            collection.delete_one(**data_insert)
        except Exception as error:
            raise str(error)

    @classmethod
    def insert_many(cls, data: dict = None):
        """Inser many data from collection"""
        collection = cls.get_collection()
        data = copy.deepcopy(data) or {}
        try:
            value = collection.insert_many(
                data,
                ordered=False
            )
        except Exception as error:
            raise str(error)

        return value
