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
        for data in file:

            question_id = data["question_id"]
            exam_id = data["exam_id"]

            name_sufix = f"0{question_id}" if question_id < 10 else str(question_id)

            name = exam_id + name_sufix
            
            logger.info(f"Uploading over question {name} ...")
            database.upsert_data(
                data,
                "questions",
                name
            )