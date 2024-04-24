from google.cloud import bigquery
import os
import logging

class BigQuery():

    def __init__(self):

        self.logger = logging.getLogger('log_decorator.BigQuery')

        self.client = bigquery.Client(project = os.getenv("PROJECT_ID"))
        self.dataset = self.client.dataset(os.getenv("DATASET_NAME"))

    def set_LoadJobConfig(self, source_format = "NEWLINE_DELIMITED_JSON", write_disposition = "WRITE_APPEND"):

        self.job_config = bigquery.LoadJobConfig(
            source_format = source_format,
            write_disposition = write_disposition
        )

        self.logger.info("Load job successfully configured!")

    def json_load_to_table(self, file, schema, table_name):

        self.logger.info("Adding schema to job config ...")
        self.job_config.schema = schema

        self.logger.info("Adding destination table to job config ...")
        table = self.dataset.table(table_name)

        self.logger.info("Loading JSON file to BigQuery table ...")
        job = self.client.load_table_from_json(
            file, 
            table, 
            job_config = self.job_config
        )

        job.result()

        self.logger.info("JSON file successfully loaded to BigQuery table!")
