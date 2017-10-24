import boto3
import botocore
import json

from scriptlets.scriptlet_global import Global


class ScriptletRekognition:
    def __init__(self, collection, bucket, region, profile=""):
        self.collection = collection
        self.bucket = bucket
        self.region = region
        self.profile = profile
        if self.profile == "":
            self.rekognition = boto3.Session(region_name=self.region).client('rekognition')
        else:
            self.rekognition = boto3.Session(profile_name=self.profile, region_name=self.region).client('rekognition')

    def list_collections(self):
        response = self.rekognition.list_collections()
        return response

    def detect_faces(self, s3_key):
        response = self.rekognition.detect_faces(
            Image={
                'S3Object': {
                    'Bucket': self.bucket,
                    'Name': s3_key
                }
            },
            Attributes=['ALL']
        )
        return response

    def index_face(self, s3_key, id):
        response = self.rekognition.index_faces(
            CollectionId=self.collection,
            Image={
                'S3Object': {
                    'Bucket': self.bucket,
                    'Name': s3_key
                }
            },
            ExternalImageId=id,
            DetectionAttributes=['ALL']
        )
        return response

    def search_face(self, s3_key):
        response = self.rekognition.search_faces_by_image(
            CollectionId=self.collection,
            Image={
                'S3Object': {
                    'Bucket': self.bucket,
                    'Name': s3_key
                }
            },
            MaxFaces=1
        )
        # return response
        return response['FaceMatches'][0]['Face']['ExternalImageId']

