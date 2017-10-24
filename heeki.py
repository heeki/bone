import boto3
import json
import os
import pprint

from scriptlets.scriptlet_s3 import ScriptletS3
from scriptlets.scriptlet_rekognition import ScriptletRekognition

bucket = os.environ['BONE_S3']
region = os.environ['BONE_REGION']
profile = os.environ['BONE_PROFILE']
role = os.environ['BONE_IAM_ROLE']
collection = os.environ['BONE_REK_COLLECTION']
pp = pprint.PrettyPrinter(indent=4)


def test_s3():
    file = "temp/test.txt"
    s3 = ScriptletS3(bucket, profile)
    s3.upload_object(file, 'heeki/test.txt')
    s3.download_object('temp/download.txt', 'heeki/test.txt')
    s3.read_file('temp/download.txt')


def test_rekognition():
    mapping = {
        'images/heeki.jpeg': 'heeki',
        'images/joe.jpeg': 'woznij'
    }
    s3_key = 'images/heeki.jpeg'

    s3 = ScriptletS3(bucket, profile)
    s3.download_object('temp/heeki.jpeg', 'images/heeki.jpeg')

    rek = ScriptletRekognition(collection, bucket, profile)
    # rek.list_collections()

    # for image in mapping:
    #     response = rek.index_face(image, mapping[image])
    #     pp.pprint(response)

    # response = rek.detect_faces(s3_key)
    # pp.pprint(response)

    response = rek.search_face(s3_key)
    pp.pprint(response)


def main():
    print "environment variables"
    print "BONE_S3={}".format(bucket)
    print "BONE_REGION={}".format(region)
    print "BONE_PROFILE={}".format(profile)
    print "BONE_IAM_ROLE={}".format(role)
    print "BONE_REK_COLLECTION={}".format(collection)

    # test_s3()
    test_rekognition()


if __name__ == '__main__':
    main()

