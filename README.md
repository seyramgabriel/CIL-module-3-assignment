# Purpose
This repository was created to detail out steps taken to perform tasks in an assignment given at module 3 of CIL academy cloud engineering programme, cohort 6.

# Tasks in the Assignment
•	Provision a t2.micro EC2 instance (Amazon Linux 2 AMI) and an S3 bucket using AWS cloudformation.
•	The EC2 instance must be assigned an IAM role to allow access via SSM instead of SSH (NO Key Pairs).
•	Upload some lovely pictures into the S3 bucket created in first task.
•	SSM into the EC2 instance and copy the contents of the S3 bucket into a DIRECTORY within your home directory called "mys3backup" (e.g. /home/blessing/mys3backup)
•	Write a Python Script that copies the S3 content to that directory on execution
•	Set up a cron job to execute the Python Script at least once every day at a time of your choosing - morning, noon, or night.
•	As a plus - write up a small design description to show what you have achieved. If you add a picture, you save a thousand words 

# Fulfilling the tasks
1. Cloudformation is an AWS service that makes it easier to create and manage virtual resources using templates. A template is a code written in yaml or json format to provision several resources in a single unit, called stack. In this assignment, the stack was made up of an amazon linux 2 ec2 instance and an s3 bucket.
   
![ec2-s3-stack](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/7182ac1f-edc3-4e6e-be9a-07ecab925f15)

The template is uploaded 

![Upload_yaml_file](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/d942febb-5252-4887-b5d1-5d32f1a40383)


The stack is created and the resources therein provisioned

![stack_and_resources_created](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/848c9de0-59e6-4145-ab68-528853ca7604)

2. Pictures are uploaded into the s3 bucket created.

![Picture_upload](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/7ceffe73-a092-4ca8-a62a-3c7e2b39eec1)


3. The instance ID is used to SSM into the ec2 instance created via cloudshell.  The SSM IAM role assigned to the ec2 instance allows us to SSM into the virtual machine without having use for keypairs...  


![INSTANCE_ID](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/27f27c83-a027-48d6-9f2b-51a11a3b7d29)


...by running " aws ssm start-session --target INSTANCE-ID"

![SSM](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/cdb3249c-f553-4243-a8da-639b65b69601)


4.Whiles in the VM, cd into your home directory (cd ~), create a directory named "mys3backup" (mkdir mys3backup) 

5. Configure your VM with access and secret access keys,default region and output format (aws configure). This is important in order to run 'aws' commands and without which access to your bucket will be denied.

   ![aws_configure](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/c4830e52-49ca-4d20-a795-db46743c6822)

6. Execute s3 sync s3://bucketname /home/ssm-user/mys3backup, replacing bucketname with the s3 bucket created.
This will download all objects (the pictures) in s3 bucket uploaded under step 2, into mys3backup directory, created in step 4.

![download_from_bucket](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/9590a437-38df-4be2-a09a-78f2f18080ee)


8. Install pip package manager by running "sudo yum install pip" then use pip to install boto3 "pip install boto3". This is a prerequisite to successfully run a python script in your ec2 instance, amazon linux 2, which already has python.

![Install_pip_and_boto3](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/93c27d74-3a3b-498a-b013-8c257a84bd99)


9. Create a .py script with the following, replacing bucket name and region. 
import boto3
import os

s3_bucket_name = 'bucketname'  
local_directory = '/home/ssm-user/mys3backup'

def copy_s3_bucket_contents():
    try:
        
        session = boto3.Session()
        s3 = session.client('s3', region_name='us-east-2')
      
        if not os.path.exists(local_directory):
            os.makedirs(local_directory)
      
        objects = s3.list_objects_v2(Bucket=s3_bucket_name)
       
        for obj in objects.get('Contents', []):
            s3_object_key = obj['Key']
            local_file_path = os.path.join(local_directory, os.path.basename(s3_object_key))

            s3.download_file(s3_bucket_name, s3_object_key, local_file_path)
            print('Copied: {} to {}'.format(s3_object_key, local_file_path))

        print('S3 bucket contents copied to the local directory successfully.')

    except Exception as e:
        print('Error: {}'.format(e))

if __name__ == '__main__':
    copy_s3_bucket_contents()

10. Run the python script (python python_script.py). Be sure to upload more files into s3 bucket before running the script to confirm successful download upon running the script.


![Run_python_script](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/0d394058-2883-4f11-892d-2674cd6680f0)


   
11. Open the cronjob editor (crontab -e) and input this cronjob to run python_script.py at 7:30pm each day
30 19 * * * /usr/bin/python /home/ssm-user/mys3backup/python_script.py



![The_cronjob](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/3b64688e-f930-435a-95e1-d1667e3e8f7e)



# The Architure


![Architure](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/d4ac56e3-2c16-46f4-a8e5-2a3c5a464106)


# Challenges encountered
After creating the stack and entering the ec2 instance via ssm, it became a challenge understanding what to install onto the VM to allow aws and python commands. I had initially created the stack with an ubuntu AMI, which required installing aws cli with 'apt' package manager, as well as installing python. I later deleted the stack and started all over with amazon linux 2 AMI. Amazon linux 2 already had aws cli and python, but one needed to configure aws and install pip with 'yum' and then use pip to install boto3.

# Conclusion
It is exciting learning how to ssm into an ec2 instance, instead of ssh, and using  cloudshell instead of local terminal. I would encourage all to experience this, and experiment cloudformation, which indeed makes creating and managing virtual resources on AWS easier and faster, once the desired template is ready.

   
