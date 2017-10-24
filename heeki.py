import boto3
import json
import os

from scriptlets.scriptlet_s3 import ScriptletS3


def main():
    bucket = os.environ['BONE_S3']
    profile = os.environ['BONE_PROFILE']
    role = os.environ['BONE_IAM_ROLE']
    print "environment variables"
    print "BONE_S3={}".format(bucket)
    print "BONE_PROFILE={}".format(profile)
    print "BONE_IAM_ROLE={}".format(role)

    file = "temp/test.txt"
    s3 = ScriptletS3(bucket, profile)


if __name__ == '__main__':
    main()

