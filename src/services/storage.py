from google.cloud import storage
import os
import json

class Storage():

    def save_local_file (self, file, filename):

        with open(filename, 'w') as local_file:
            json.dump(file, local_file)


class GoogleCloudStorage( Storage ):

    def __init__(self):

        self.client = storage.Client()

        self.bucket_name = os.getenv("BUCKET_NAME")

        self.blob_template_name = "gcp_exam_questions/{name}"
    
    
    def upload_json_to_storage(self, file, filename, from_local_file = False, path = "./"):

        bucket = self.client.bucket(self.bucket_name)
        blob = bucket.blob(
            self.blob_template_name.format(name = filename)
        )

        if from_local_file:

            local_path = os.path.join(path, file)
            blob.upload_from_filename(local_path, content_type = 'application/json')

        else:
            file_json = json.dumps(file)
            blob.upload_from_string(file_json, content_type = 'application/json')

    def dowload_json_file (self, blob_name):
        
        bucket = self.client.bucket(self.bucket_name)
        blob = bucket.blob(
            blob_name
        )

        file = blob.download_as_bytes()

        return json.loads(file)
