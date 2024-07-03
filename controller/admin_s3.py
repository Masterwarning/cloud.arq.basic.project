import boto3
import boto3.session
from credentials.keys import ACCESS_KEY, SECRET_KEY
import tempfile

bucket_name = "bucket-project-cloudvet"
url_photos = "https://bucket-project-cloudvet.s3.amazonaws.com/photos/"

def connect_s3():
    try:
        session_aws = boto3.session.Session(ACCESS_KEY, SECRET_KEY)
        s3_resource =session_aws.resource('s3')
        print("admin_s3.connect_s3: Conexion S3 exitosa")
        return s3_resource
    except Exception as error:
        print("admin_s3.connect_s3: error en la conexion -", error)
        return None
    
def save_photo(photo):
    try:
        file_name = photo.filename
        if len(file_name.split(".")) == 1:
            return None
        extension = file_name.split(".")[-1]
        #photo_path = "/temp/picture." + extension #linux
        photo_path = tempfile.gettempdir() + "\picture." + extension #windows
        photo.save(photo_path)
        print("admin_s3.save_photo: Foto almacenada en directorio temporal")
        return photo_path
    except Exception as error:
        print("admin_s3.save_photo: error -", error)
        return None
    
def upload_s3(local_path, photo, id):
    try:
        s3_resource = connect_s3()
        file_name = photo.filename
        extension = file_name.split(".")[-1]
        bucket_path = "photos/" + id + "." + extension
        s3_resource.meta.client.upload_file(local_path, bucket_name, bucket_path)
        print("admin_s3.upload_s3: Foto almacenada en bucket S3")
        return True
    except Exception as error:
        print("admin_s3.upload_s3: error -", error)
        return False
    
def consult_file(id):
    try:
        s3_resource = connect_s3()
        bucket_repo = s3_resource.Bucket(bucket_name)
        bucket_objects = bucket_repo.objects.filter(Prefix="photos/")

        for obj in bucket_objects:
            if id in obj.key:
                file_name = (obj.key).split("/")[-1]
                print("admin_s3.consult_file: Archivo encontrado en S3")
                return url_photos + file_name
        print("admin_s3.consult_file: Archivo no encontrado")
        return None
    
    except Exception as error:
        print("admin_s3.consult_file: error -", error)
        return None
