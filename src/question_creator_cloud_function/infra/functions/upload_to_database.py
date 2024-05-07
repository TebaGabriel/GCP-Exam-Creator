from infra.services.database import Datastore
import logging

def data_to_database(data, id):

    logger = logging.getLogger('log_decorator.data_to_database')

    logger.info("Initializing database class ...")
    database = Datastore()
    with database:
        
        logger.info(f"Uploading over question {id} ...")
        database.insert_data(
            data,
            "questions",
            id
        )