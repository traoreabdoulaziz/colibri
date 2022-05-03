import datetime
import os
import tempfile
from ...config.config import BUCKET_NAME,STORAGE_CLIENT,s3_client,s3_resource
ENV = os.environ.get('ENV')


## function to upload file to cloud storage
def save_file_to_storage(image_url,file):
    bucket=STORAGE_CLIENT.get_bucket(BUCKET_NAME)
    blob=bucket.blob(image_url+'.'+file.filename.split('.')[-1])
    blob.upload_from_file(file.file)


## function to download file to cloud storage
def download_file_to_storage(folder):
    bucket=STORAGE_CLIENT.get_bucket(BUCKET_NAME)
    key_tab=[]
    for blob in bucket.list_blobs(prefix=folder):
        key_tab.append(blob.name)
    last_file=sorted(key_tab)[-1]
    if ENV=='local':
        return last_file
    blob=bucket.get_blob(last_file)
    file_url=blob.generate_signed_url(expiration=datetime.timedelta(minutes=15),method='GET')
    return file_url
  
## verify if file exist     
def verify_file_existance(folder):
    files=STORAGE_CLIENT.list_blobs(BUCKET_NAME,prefix=folder)
    if len(list(files))==0:
        return False
    else:
        return True
    
## verify if the file exist in S3
def get_existing_fn(bucket:str, prefix:str):
    return list(s3_resource.Bucket(bucket).objects.filter(Prefix=prefix))
   

## save The file in S3
def save_file_in_S3(bucket:str, url:str, file):
    s3_resource.Object(bucket, url+'.'+file.filename.split('.')[-1]).put(Body=file.file)
    return True

##get file name in S3
def get_file_name_in_S3(url:str):
    image_name = list(s3_resource.Bucket('data354-public-assets').objects.filter(Prefix=url))[0].key
    return image_name

## get file url in S3
def get_file_url_in_S3(image_name):
    image_url = s3_client.generate_presigned_url(
                ClientMethod='get_object', 
                Params={'Bucket': 'data354-public-assets', 'Key': image_name},
                ExpiresIn=60)
    return image_url