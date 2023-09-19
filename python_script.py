#Header
import boto3
import os

#Set your AWS credentials and region
aws_access_key_id = ''
aws_secret_access_key = ''
aws_region = ''

# Set the S3 bucket name and local directory path
s3_bucket_name = 'kofiseysey'  # Replace with your S3 bucket name
local_directory = '/home/ssm-user/mys3backup'

def copy_s3_bucket_contents():
    # Initialize the S3 client
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

    try:
        # List objects in the S3 bucket
        objects = s3.list_objects_v2(Bucket=s3_bucket_name)

        # Create the local directory if it doesn't exist
        os.makedirs(local_directory, exist_ok=True)

        # Iterate through S3 objects and copy them to the local directory
        for obj in objects.get('Contents', []):
            s3_object_key = obj['Key']
            local_file_path = os.path.join(local_directory, os.path.basename(s3_object_key))

            # Download the S3 object
            s3.download_file(s3_bucket_name, s3_object_key, local_file_path)
            print(f'Copied: {s3_object_key} to {local_file_path}')

        print('S3 bucket contents copied to the local directory successfully.')

    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    copy_s3_bucket_contents()


