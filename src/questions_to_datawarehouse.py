from services.storage import GoogleCloudStorage
from datawarehouse_params import QUESTIONS_SCHEMA
import os

def questions_to_datawarehouse(request):

    storage = GoogleCloudStorage()
    file = storage.dowload_json_file(request["blob"])

    from google.cloud import bigquery
    client = bigquery.Client(project = os.getenv("PROJECT_ID"))
    dataset  = client.dataset(os.getenv("DATASET_NAME"))
    table = dataset.table("raw_questions")

    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    job_config.schema = QUESTIONS_SCHEMA

    job = client.load_table_from_json(file, table, job_config = job_config)

    print(job.result())

    return



if __name__ == "__main__":

    from dotenv import load_dotenv
    load_dotenv()

    request = {
        "blob" : "gcp_exam_questions/2024-04-18.json"
    }
    questions_to_datawarehouse(request)