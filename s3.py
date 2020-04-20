import boto3
import uuid
import os

first_bucket_name = 'firstredmanbucketc4ad44c6-a4fd-4a5a-bd8a-151bd85638d9'

#for testing
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
    return ''.join([bucket_prefix, str(uuid.uuid4())])

def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2'})
    print(bucket_name, current_region)
    return bucket_name, bucket_response

def create_temp_file(size, file_name, file_content):
    random_file_name = ''.join([str(uuid.uuid4().hex[:6]), file_name])
    with open(random_file_name, 'w') as f:
        f.write(str(file_content) * size)
    return random_file_name

#first_bucket_name, first_response = create_bucket(bucket_prefix='firstredmanbucket', s3_connection=s3_resource)

# def delete_all_objects(bucket_name):
#     res = []
#     bucket=s3_resource.Bucket(bucket_name)
#     for obj_version in bucket.object_versions.all():
#         res.append({'Key': obj_version.object_key,
#                     'VersionId': obj_version.id})
#
#     print(len(res))
    #bucket.delete_objects(Delete={'Objects': res})

#delete_all_objects(first_bucket_name)

file_name = create_temp_file(300, 'file.txt', 'f')

s3_resource.Object(first_bucket_name, file_name).upload_file(Filename=(file_name)
