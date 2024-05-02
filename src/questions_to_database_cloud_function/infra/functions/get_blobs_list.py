from datetime import datetime, timezone, timedelta
from infra.services.storage import GoogleCloudStorage
import logging

def get_last_blob_list(delta_datetime: timedelta):

    logger = logging.getLogger('log_decorator.get_last_blob_list')

    logger.info("Initializing storage class ...")
    storage = GoogleCloudStorage()

    datetime_range = datetime.now(timezone.utc) - delta_datetime

    logger.info(f"Getting blobs created after {datetime_range}")
    filtered_list = [*filter(
        lambda x: x.time_created >=  datetime_range ,
        storage.list_blobs()
    )]
    
    logger.info(f"Blobs filtered list sucessfully gotten!")
    return filtered_list
