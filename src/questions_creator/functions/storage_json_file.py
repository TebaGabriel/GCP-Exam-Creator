import logging
from datetime import datetime 
from services.storage import GoogleCloudStorage


def storage_json_file(file, local_storage = False):
    
    logger = logging.getLogger('log_decorator.storage_json_file')

    filename = datetime.now().strftime("%Y-%m-%d") + ".json"

    storage = GoogleCloudStorage(file, filename)
    
    if local_storage:

        storage.save_local_file()
        
    else:

        storage.upload_json()

    logger.info("File successfully storage!")

    return 