from services.storage import GoogleCloudStorage
from services.datawarehouse import BigQuery
from datawarehouse_params import QUESTIONS_SCHEMA

def file_to_datawarehouse(blob):

    storage = GoogleCloudStorage()
    file = storage.dowload_json_file(blob.name)

    datawarehouse = BigQuery()
    datawarehouse.set_LoadJobConfig(
            source_format = "NEWLINE_DELIMITED_JSON",
            write_disposition = "WRITE_TRUNCATE"
        )
    
    datawarehouse.json_load_to_table(
            file,
            QUESTIONS_SCHEMA,
            "raw_questions"
        )
    