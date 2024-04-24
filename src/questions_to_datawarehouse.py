import os
from datetime import timedelta
from functions.get_blobs_list import get_last_blob_list
from functions.file_to_datawarehouse import file_to_datawarehouse
from services.logger import log
import logging

@log
def questions_to_datawarehouse(request):

    logger = logging.getLogger('log_decorator.questions_to_datawarehouse')

    HOURS_RANGE = 2

    logger.info(f"Set time range to {HOURS_RANGE} hours ago!")
    datetime_range = timedelta(days = HOURS_RANGE)
    
    logger.info("Getting blobs in time range...")
    blobs = get_last_blob_list(datetime_range)

    for blob in blobs:
        logger.info(f"Uploading {blob.name} to datawarehouse ...")
        file_to_datawarehouse(blob)

    return



if __name__ == "__main__":

    from dotenv import load_dotenv
    load_dotenv()

    questions_to_datawarehouse(None)