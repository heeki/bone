import boto3
import botocore
import json
import os

from scriptlets.scriptlet_global import Global


class ScriptletS3:
    def __init__(self, bucket, profile=""):
        self.log = Global.get_logger("hackathon", "logs/hackathon.log")
        self.profile = profile
        if self.profile == "":
            self.bucket = boto3.resource('s3').Bucket(bucket)
        else:
            self.bucket = boto3.Session(profile_name=self.profile).resource('s3').Bucket(bucket)

    def _skip(self, root, file_local):
        """ Determine if a file should be filtered out

        :param root: base directory
        :param file_local: file to be evaluated
        :return: boolean, if file should be filtered out
        """
        skip = False
        if file_local.startswith('.') or file_local.startswith('_') or file_local.endswith('.pyc'):
            skip = True
        if '/.' in root:
            skip = True
        return skip

    def upload_dir(self, path_local, prefix):
        """ Upload a directory to S3 bucket

        :param path_local: local directory from which data will be uploaded
        :param prefix: S3 bucket prefix
        :return: none
        """
        for root, dirs, files in os.walk(path_local):
            for f in files:
                if self._skip(root, f):
                    continue
                path_source = os.path.join(root, f)
                key = "{}/{}".format(prefix, f)
                if path_local == '.':
                    path_source = f
                self.upload_object(path_source, key)

    def upload_object(self, path_local, key):
        """ Upload a directory to an S3 bucket

        :param path_local: full path to local source file
        :param key: full path to target S3 bucket location
        :return: none
        """
        self.log.info("upload_object(): uploading source={} to bucket={} key={}".format(path_local, self.bucket.name, key))
        self.bucket.upload_file(path_local, key)

    def download_object(self, path_local, key):
        """ Download a file from an S3 bucket

        :param path_local: full path to target local location to save the file
        :param key: full path to source S3 file
        :return: none
        """
        try:
            self.bucket.download_file(key, path_local)
        except botocore.exceptions.ClientError as e:
            self.log.error("download_object(): {}".format(e))

    def list_objects(self, logging=True):
        """ Download a file from an S3 bucket

        :return: none
        """
        if logging:
            for obj in self.bucket.objects.all():
                self.log.info("list_objects(): found {}".format(obj.key))
        return self.bucket.objects.all()

    def delete_objects(self, objects):
        """ Delete a list of objects

        :param objects: list of objects to be deleted
        :return: none
        """
        body = dict()
        body["Objects"] = []
        for obj in objects:
            self.log.info("delete_objects(): will delete {}".format(obj))
            body["Objects"].append({'Key': obj})
        response = self.bucket.delete_objects(Delete=body)
        print json.dumps(response, indent=4, sort_keys=True)

    def read_file(self, path_local):
        """ Read from a local file

        :param path_local: local file path
        :return: JSON object read from the local file
        """
        if os.path.isfile(path_local):
            with open(path_local, 'r') as file_local:
                self.log.info("read_file(): reading file {}".format(path_local))
                data = file_local.read()
                json_obj = json.loads(data)
                # print json.dumps(json_obj, indent=4, sort_keys=True)
                return json_obj

    def write_file(self, path_local, json_obj):
        """ Write to a local file

        :param path_local: local file path
        :param json_obj: JSON object to write to the local file
        :return: none
        """
        with open(path_local, 'w') as file_local:
            file_local.write(json.dumps(json_obj, indent=4, sort_keys=True))

