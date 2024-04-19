from google.cloud import bigquery
import os

class BigQuery():

    def __init__(self):

        self.client = bigquery.Client(project = os.getenv("PROJECT_ID"))
        self.dataset = self.client.dataset(os.getenv("DATASET_NAME"))

    def set_LoadJobConfig(self, source_format = "NEWLINE_DELIMITED_JSON", write_disposition = "WRITE_APPEND"):

        self.job_config = bigquery.LoadJobConfig(
            source_format = source_format,
            write_disposition = write_disposition
        )

    def json_load_to_table(self, file, schema, table_name):

        self.job_config.schema = schema

        table = self.dataset.table(table_name)

        job = self.client.load_table_from_json(
            file, 
            table, 
            job_config = self.job_config
        )

        return job.result()
