import boto3
import os
from boto3 import client
from botocore.exceptions import ClientError
from cred import access_key, secret_access_key

client = boto3.client('s3', aws_access_key_id = access_key, aws_secret_access_key = secret_access_key)
my_bucket = 'mediasx'

path_images = "/home/shubhxluzive/PycharmProjects/py_cloud_projects/in-images"
path_videos = "/home/shubhxluzive/PycharmProjects/py_cloud_projects/in-videos"

def upload_single_file(file_name, object_name=None):
    if object_name is None:
        object_name = file_name
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, my_bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

current_images_in_bucket = [image['Key'] for image in client.list_objects(Bucket=my_bucket)['Contents'] if (image['Key'][-3:]=='jpg')]
current_videos_in_bucket = [video['Key'] for video in client.list_objects(Bucket=my_bucket)['Contents'] if (video['Key'][-3:]=='mp4')]

def upload_all_images():
    for file in os.listdir(path_images):
        if '.jpg' in file and file not in current_images_in_bucket:
            upload_file_key = str(file)
            client.upload_file(file, my_bucket, upload_file_key)

def upload_all_videos():
    for video in os.listdir(path_videos):
        if '.mp4' in file and video not in current_videos_in_bucket:
            upload_video_key = str(video)
            client.upload_file(video, my_bucket, upload_video_key)


def all_images_download():
    for key in client.list_objects(Bucket=my_bucket)['Contents']:
        if '.jpg' in key['Key']:
            client.download_file('mediasx', key['Key'], 'out-images/' + str(key['Key']))
    print("All the images with extension '.jpg' have been downloaded in 'out-images' folder. ")
def all_videos_download():
    for key in client.list_objects(Bucket=my_bucket)['Contents']:
        if '.mp4' in key['Key']:
            client.download_file('mediasx', key['Key'], 'out-video/' + str(key['Key']))
        print(key['Key'])


upload_all_images()
upload_all_videos()

print("1. Press 1 to upload single file from 'in-image' folder.")
print("2. Press 2 to download all images in 'out-images' folder.")
print("3. Press 3 to download all videos in 'out-video' folder.")
print("4. Press 4 to exit the program \n")
user_input = int(input("Choose one 1, 2, 3 or 4: "))
choices = [1, 2, 3, 4]
if user_input in choices :
    if user_input == 1:
        print("enter file name to be upload")
        file_name = input()
        upload_single_file(file_name)
        print("Chosen file has been uploaded successfully.")
    elif user_input == 2:
        all_images_download()
    elif user_input == 3:
        all_videos_download()
    elif user_input == 4:
        exit()
else:
    print("Entered wrong input, please choose correct option (1, 2, 3 or 4")




