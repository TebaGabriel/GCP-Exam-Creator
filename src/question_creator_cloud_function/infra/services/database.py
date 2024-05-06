from google.cloud import datastore
import os
import logging

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

    def upsert_data (self, data: dict, kind, name = None):


        key = self.client.key(kind, name)

        entity = datastore.Entity(key = key)

        self.logger.info(f"Uploading {kind} Kind and {name} name entity ...")

        entity.update(
            data
        )

        self.client.put(entity)
        self.logger.info("Data successfully upserted!")