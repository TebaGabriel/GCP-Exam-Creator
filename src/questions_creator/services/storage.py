from google.cloud import storage
import os
import json

class Storage():

    def __init__(self, file, storage_filename):

        self.file = file

        self.storage_filename = storage_filename


    def save_local_file (self):

        with open(self.storage_filename, 'w') as local_file:
            json.dump(self.file, local_file)


class GoogleCloudStorage( Storage ):

    def __init__(self, file, storage_filename):

        super().__init__(file, storage_filename)

        self.client = storage.Client()

        self.bucket_name = os.getenv("BUCKET_NAME")

        self.blob_template_name = "gcp_exam_questions/{name}"
    
    
    def upload_json(self, from_local_file = False, path = "./"):

        bucket = self.client.bucket(self.bucket_name)
        blob = bucket.blob(
            self.blob_template_name.format(name = self.storage_filename)
        )

        if from_local_file:

            filename = os.path.join(path, self.file)
            blob.upload_from_filename(filename, content_type = 'application/json')

        else:
            file_json = json.dumps(self.file)
            blob.upload_from_string(file_json, content_type = 'application/json')