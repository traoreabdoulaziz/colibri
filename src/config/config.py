import json
import os

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"]= "colibri-test-349114-a30e8b514e6d.json"
# os.environ['ENV']="dev"
ENV = os.environ.get("ENV")
with open("secrets.json", "r") as f:
    secret = json.load(f)[ENV]


from google.cloud import ndb
import boto3
from google.cloud import storage
from google.cloud import firestore
import fireorm
import firebase_admin
import tempfile
from google.auth.credentials import AnonymousCredentials
from google.cloud import storage
from google.api_core.client_options import ClientOptions


### GLOBALE CONFIG CLOUD STORAGE
# api_endpoint="http://storage:4443/"
if ENV == "local":
    options = ClientOptions(api_endpoint="http://storage:4443/")
    STORAGE_CLIENT = storage.Client(
        credentials=AnonymousCredentials(), client_options=options
    )
if ENV == "dev" or ENV == "staging":
    STORAGE_CLIENT = storage.Client()
BUCKET_NAME = secret["BUCKET_NAME"]


## gcloud firestore
if ENV == "local":
    os.environ["FIRESTORE_EMULATOR_HOST"] = "firestore:8080"
firebase_admin.initialize_app()
FIRESTORE_DB = firestore.Client()
fireorm.connect(FIRESTORE_DB)


## auth credentials
JWT_SECRET = secret["JWT_SECRET"]
ACCESS_TOKEN_EXPIRE_MINUTES = secret["ACCESS_TOKEN_EXPIRE_MINUTES"]


# S3 bucket config
REGION_NAME = "eu-west-3"
AWS_ACCESS_KEY_ID = "AKIA2KH2OIGSVTEZV4UX"
AWS_SECRET_ACCESS_KEY = "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"
s3_resource = boto3.resource(
    "s3",
    region_name=REGION_NAME,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)
s3_client = boto3.client(
    "s3",
    region_name=REGION_NAME,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)
