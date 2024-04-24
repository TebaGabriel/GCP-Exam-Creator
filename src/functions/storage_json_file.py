import logging
from datetime import datetime, timezone
from services.storage import GoogleCloudStorage

def storage_json_file(file, local_storage = False):
    
    logger = logging.getLogger('log_decorator.storage_json_file')

    filename = datetime.now(timezone.utc).strftime("%Y-%m-%d") + ".json"
    logger.info(f"Create filename as {filename}")

    logger.info("Initializing storage class ...")
    storage = GoogleCloudStorage()
    
    if local_storage:

        logger.warn("Set storage as local!!")

        storage.save_local_file(file, filename)
        
    else:

        logger.info("Uploading json file to Storage ...")
        storage.upload_json_to_storage(file, filename)


    return 