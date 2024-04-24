from services.storage import GoogleCloudStorage
from services.datawarehouse import BigQuery
from datawarehouse_params import QUESTIONS_SCHEMA
import logging

def file_to_datawarehouse(blob):

    logger = logging.getLogger('log_decorator.file_to_datawarehouse')

    logger.info("Initializing storage class ...")
    storage = GoogleCloudStorage()

    logger.info("Downloading file from storage ...")   
    file = storage.dowload_json_file(blob.name)

    logger.info("Initializing datawarehouse class ...")   
    datawarehouse = BigQuery()

    logger.info("Seting load job to JSON file ...")
    datawarehouse.set_LoadJobConfig(
            source_format = "NEWLINE_DELIMITED_JSON",
            write_disposition = "WRITE_TRUNCATE"
        )
    
    logger.info("Uploading JSON file to datawarehouse ...")
    datawarehouse.json_load_to_table(
            file,
            QUESTIONS_SCHEMA,
            "raw_questions"
        )
    