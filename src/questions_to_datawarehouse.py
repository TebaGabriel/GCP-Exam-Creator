from services.datawarehouse import BigQuery
from services.storage import GoogleCloudStorage
from datawarehouse_params import QUESTIONS_SCHEMA
import os

def questions_to_datawarehouse(request):

    storage = GoogleCloudStorage()
    file = storage.dowload_json_file(request["blob"])


    datawarehouse = BigQuery()
    datawarehouse.set_LoadJobConfig(
        source_format = "NEWLINE_DELIMITED_JSON",
        write_disposition = "WRITE_TRUNCATE"
    )
    response = datawarehouse.json_load_to_table(
        file,
        QUESTIONS_SCHEMA,
        "raw_questions"

    )

    print(response)

    return



if __name__ == "__main__":

    from dotenv import load_dotenv
    load_dotenv()

    request = {
        "blob" : "gcp_exam_questions/2024-04-18.json"
    }
    questions_to_datawarehouse(request)