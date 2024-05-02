from infra.services.storage import GoogleCloudStorage
from infra.services.database import Datastore
import logging

def file_to_database(blob):

    logger = logging.getLogger('log_decorator.data_to_database')

    logger.info("Initializing storage class ...")
    storage = GoogleCloudStorage()

    logger.info("Downloading file from storage ...")   
    file = storage.dowload_json_file(blob.name)
    
    logger.info("Setting template name ...")

    logger.info("Initializing database class ...")
    database = Datastore()
    with database as db:

        logger.info("Iterating over questions ...")
        for id in range(len(file)):

            name_sufix = f"0{id+1}" if id < 9 else str(id+1)

            name = file[id]["exam_date"] + name_sufix
            
            logger.info(f"Uploading over question {name} ...")
            database.upsert_data(
                file[id],
                "questions",
                name
            )