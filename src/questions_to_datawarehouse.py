import os
from datetime import timedelta
from functions.get_blobs_list import get_last_blob_list
from functions.file_to_datawarehouse import file_to_datawarehouse


def questions_to_datawarehouse(request):

    
    datetime_range = timedelta(hours = 1)
    blobs = get_last_blob_list(datetime_range)

    for blob in blobs:
        file_to_datawarehouse(blob)

    return



if __name__ == "__main__":

    from dotenv import load_dotenv
    load_dotenv()

    questions_to_datawarehouse(None)