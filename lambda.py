import boto3
import json
import os
from scriptlets.scriptlet_rekognition import ScriptletRekognition


def lambda_handler(event, context):
    print "Received event: {}".format(json.dumps(event, indent=2))
    print "Received context: {}".format(str(context))

    print "Logging information: {}, {}".format(context.log_group_name, context.log_stream_name)
    print "Request id: {}".format(context.aws_request_id)
    print "Memory limit (MB): {}".format(context.memory_limit_in_mb)

    speech_topic_arn = os.environ['SPEECH_TOPIC_ARN']
    collection = os.environ['BONE_REK_COLLECTION']
    index_bucket = os.environ['INDEX_BUCKET']
    search_bucket = os.environ['SEARCH_BUCKET']

    try:
        for record in event['Records']:
            s3_bucket = record['s3']['bucket']['name']
            image_key = record['s3']['object']['key']
            external_id = image_key.split(".")[0]
            r_searcher = ScriptletRekognition(collection, s3_bucket)
            
            if s3_bucket == index_bucket:
                r_searcher.index_face(image_key, external_id)

            # Call image search
            if s3_bucket == search_bucket:
                found_alias = r_searcher.search_face(image_key)

            if found_alias:
                sns = boto3.client('sns')
                sns.publish(
                    TopicArn=speech_topic_arn,
                    Message=JSON.dumps({'alias_name: alias_name})
                )
    except KeyError as ke:
        print("Input object is not formatted correctly. Error: %s", str(ke))

    response = {
        'statusCode': 200,
        'headers': {},
        'body': body
    }
    return response
