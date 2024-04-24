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

class GoogleCloudStorage( Storage ):

    def __init__(self):

        super().__init__()

        self.client = storage.Client()

        self.bucket_name = os.getenv("BUCKET_NAME")

        self.blob_prefix = "gcp_exam_questions/"
    
    
    def upload_json_to_storage(self, file, filename, from_local_file = False, path = "./"):

        self.logger.info("Seting bucket ...")
        bucket = self.client.bucket(self.bucket_name)

        self.logger.info("Seting blob ...")
        blob = bucket.blob(
            self.blob_template_name + filename
        )

        if from_local_file:

            self.logger.warn("Upload mode from local file!")
            
            local_path = os.path.join(path, filename)
            self.logger.info(f"Set file path as {local_path}!")

            self.logger.info(f"Uploading local file to Cloud Storage ...")
            blob.upload_from_filename(local_path, content_type = 'application/json')

        else:

            self.logger.info("Parsing file to JSON ...")
            file_json = json.dumps(file)

            self.logger.info(f"Uploading file to Cloud Storage ...")
            blob.upload_from_string(file_json, content_type = 'application/json')
            
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