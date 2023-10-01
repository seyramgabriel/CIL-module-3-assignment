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

# Fulfilling the Tasks
1. Cloudformation is an AWS service that makes it easier to create and manage virtual resources using templates. A template is a code written in yaml or json format to provision several resources in a single unit, called stack. In this assignment, the stack was made up of an amazon linux 2 ec2 instance and an s3 bucket.

    The template:   
![ec2-s3-stack](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/7182ac1f-edc3-4e6e-be9a-07ecab925f15)

    The template is uploaded:
![Upload_yaml_file](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/d942febb-5252-4887-b5d1-5d32f1a40383)


    The stack is created and the resources therein provisioned:
![stack_and_resources_created](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/848c9de0-59e6-4145-ab68-528853ca7604)


2. Upload pictures into the s3 bucket created.
![Picture_upload](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/218af247-ec41-49d3-b6b5-1fa277fbb7dc)


3. The instance ID is used to SSM into the ec2 instance created via cloudshell.  The SSM IAM role assigned to the ec2 instance allows us to SSM into the virtual machine without having use for keypairs. 
![INSTANCE_ID](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/27f27c83-a027-48d6-9f2b-51a11a3b7d29)


   Run "aws ssm start-session --target INSTANCE-ID":
![SSM](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/cdb3249c-f553-4243-a8da-639b65b69601)


4. Whiles in the VM, cd into your home directory (cd ~), create a directory named "mys3backup" (mkdir mys3backup). 

5. Configure your VM (run aws configure) with access and secret access keys, default region and output format , without which access to your bucket will be denied.
![aws_configure](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/c4830e52-49ca-4d20-a795-db46743c6822)

6. Execute "s3 sync s3://bucketname /home/ssm-user/mys3backup", replacing bucketname with the s3 bucket created.
This will download all objects (the pictures) in s3 bucket uploaded under step 2, into mys3backup directory, created in step 4.

![download_from_bucket](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/9590a437-38df-4be2-a09a-78f2f18080ee)


7. Install pip package manager by running "sudo yum install pip" then use pip to install boto3 "pip install boto3". This is a prerequisite to successfully run the python script, since boto3 is the AWS SDK for python, even though amazon linux 2 comes preinstalled with python.

![Install_pip_and_boto3](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/93c27d74-3a3b-498a-b013-8c257a84bd99)


8. Create a .py script with the following, replacing bucket name and region:  
![python_script](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/809ab54b-f730-4ba7-b736-2c5f30177769)


9. Run the python script (python python_script.py). Be sure to upload more files into s3 bucket before running the script to confirm successful download upon running the script.
![Run_python_script](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/0d394058-2883-4f11-892d-2674cd6680f0)


   
10. Open the cronjob editor (crontab -e) and input this cronjob to run python_script.py at 7:30pm each day
"30 19 * * * /usr/bin/python /home/ssm-user/mys3backup/python_script.py"
![The_cronjob](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/3b64688e-f930-435a-95e1-d1667e3e8f7e)



# The Architecture
![Architure](https://github.com/seyramgabriel/CIL-module-3-assignment/assets/130064282/d4ac56e3-2c16-46f4-a8e5-2a3c5a464106)


# Challenges Encountered
After creating the stack and entering the ec2 instance via ssm, it became a challenge understanding what to install onto the VM to allow aws and python/boto3 commands. I had initially created the stack with an ubuntu AMI, which required installing aws cli with 'apt' package manager, as well as installing python. I later deleted the stack and started all over with amazon linux 2 AMI. Amazon linux 2 comes with aws cli and python pre-installed, but one needs to configure aws and install pip with 'yum' and then use pip to install boto3.

Getting an archectural diagram and uploading pictures to github was also challenge, but thanks to @DelaDoreen who assisted in this regard.

Essentially, the above challenges and overcoming them, in my estimation, form the crux of the assignment.

# Conclusion
It is exciting learning how to ssm into an ec2 instance, instead of ssh, and using  cloudshell instead of local terminal. I would encourage all to experience this, and experiment cloudformation, which indeed makes creating and managing virtual resources on AWS easier and faster, once the desired template is ready.

# Going Forward
I get elated whenever I press enter and meet with success on the terminal. I love to work with codes. This assignment makes me want to explore the aws cloudformation documentation to experiment with a lot more virtual resources and that is exactly what I look forward to doing. 

   
