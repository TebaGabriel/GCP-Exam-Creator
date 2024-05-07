from google.cloud import datastore
import os
import logging
from datetime import datetime, timezone


class Datastore():

    def __init__ (self):

        self.logger = logging.getLogger('log_decorator.datastore')

        self.client = datastore.Client(
            project = os.getenv("PROJECT_ID"),
            database = os.getenv("DATASTORE_DATABASE")
            )
        
    def __enter__(self):

        self.logger.info("Initializing transaction datastore mode ...")
        self.client.transaction()


    def __exit__ (self,  exc_type, exc_val, exc_tb):

        pass

    def insert_data (self, data: dict, kind, name = None):


        key = self.client.key(kind, name)

        entity = datastore.Entity(key = key)

        self.logger.info(f"Uploading {kind} Kind and {name} name entity ...")

        created_datetime = datetime.now(timezone.utc)
        
        entity["created_at"] = created_datetime
        entity["updated_at"] = created_datetime

        entity.update(
            data
        )

        self.client.put(entity)
        self.logger.info("Data successfully upserted!")


    def update_data (self, data, kind, name):

        key = self.client.key(kind, name)

        self.logger.info(f"Get {kind} Kind and {name} name entity ...")
        entity = self.client.get(key)

        for field, value in data.items():
            entity[field] = value

        updated_datetime = datetime.now(timezone.utc)
        entity["updated_at"] = updated_datetime

        self.client.put(entity)

        self.logger.info("Data successfully updated!")


    def query_data (self, kind, *args):

        query = self.client.query(kind = kind)

        for filter in args:

            query.add_filter(filter=(filter["field"], filter["operator"], filter["value"]))

        return [*query.fetch()]
