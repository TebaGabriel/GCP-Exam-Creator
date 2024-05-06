from infra.services.database import Datastore
import logging

def data_to_database(data):

    logger = logging.getLogger('log_decorator.data_to_database')

    logger.info("Initializing database class ...")
    database = Datastore()
    with database as db:

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