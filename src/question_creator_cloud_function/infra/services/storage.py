from google.cloud import storage
import os
import json
import logging

class Storage():

    def __init__ (self):
        
        self.logger = logging.getLogger('log_decorator.Storage')

    def save_local_file (self, file, filename, path = "./"):

        local_filename = os.path.join(path, filename)
        
        self.logger.info(f"Saving {local_filename} ...") 

        with open(local_filename, 'w') as local_file:
            json.dump(file, local_file)

        self.logger.info(f"{local_filename} successfully saved!")

        return local_filename

class GoogleCloudStorage( Storage ):

    def __init__(self):

        super().__init__()

        self.client = storage.Client()

        self.bucket_name = os.getenv("BUCKET_NAME")

        self.blob_prefix = "gcp_exam_questions/"
    
    
    def upload_json_to_storage(self, file, filename):

        self.logger.info("Seting bucket ...")
        bucket = self.client.bucket(self.bucket_name)

        self.logger.info("Seting blob ...")
        blob = bucket.blob(
            self.blob_prefix + filename
        )

        self.logger.warn("Saving file locally ...")

        local_path = self.save_local_file(file, filename, path="/tmp")

        self.logger.info(f"Uploading local file to Cloud Storage ...")
        blob.upload_from_filename(local_path, content_type = 'application/json')
        
        self.logger.info(f"File sucessfully uploaded to Cloud Storage")

    def dowload_json_file (self, blob_name):
        
        self.logger.info("Seting bucket ...")
        bucket = self.client.bucket(self.bucket_name)

        self.logger.info("Seting blob ...")
        blob = bucket.blob(
            blob_name
        )

        self.logger.info("Dowloading file from blob ...")
        file = blob.download_as_bytes()

        self.logger.info("File successfully dowloaded!")
        return json.loads(file)
    
    def list_blobs(self):

        self.logger.info("Getting blobs lists in bucket ...")
        blobs_list = self.client.list_blobs(self.bucket_name, prefix=self.blob_prefix, delimiter="/")

        self.logger.info("Blobs lists successfully gotten!")

        return [*blobs_list]