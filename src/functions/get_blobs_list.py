from datetime import datetime, timezone, timedelta
from services.storage import GoogleCloudStorage

def get_last_blob_list(delta_datetime: timedelta):

    datetime_range = datetime.now(timezone.utc) - delta_datetime  
    storage = GoogleCloudStorage()

    filtered_list = [*filter(
        lambda x: x.time_created >=  datetime_range ,
        storage.list_blobs()
    )]
    

    return filtered_list
