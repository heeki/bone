import boto3
import json
import os


def main():
    bucket = os.environ['BONE_S3']
    role = os.environ['BONE_IAM_ROLE']
    print "environment variables"
    print "BONE_S3={}".format(bucket)
    print "BONE_IAM_ROLE={}".format(role)

if __name__ == '__main__':
    main()

