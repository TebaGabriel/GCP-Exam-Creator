from datetime import timedelta
from infra.functions.get_blobs_list import get_last_blob_list
from infra.functions.upload_to_database import file_to_database
from infra.services.logger import log
import logging

@log
def questions_to_database(request):

    logger = logging.getLogger('log_decorator.questions_to_database')

    HOURS_RANGE = 1

    logger.info(f"Set time range to {HOURS_RANGE} hours ago!")
    datetime_range = timedelta(hours = HOURS_RANGE)
    
    logger.info("Getting blobs in time range...")
    blobs = get_last_blob_list(datetime_range)

    for blob in blobs:
        logger.info(f"Uploading {blob.name} to datawarehouse ...")
        file_to_database(blob)

    return {
        "status_code": 200,
        "message": "Success"
    }



if __name__ == "__main__":

    from dotenv import load_dotenv
    load_dotenv()

    questions_to_datawarehouse(None)