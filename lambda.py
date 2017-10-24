import boto3
import json
import os


def lambda_handler(event, context):
    print "Received event: {}".format(json.dumps(event, indent=2))
    print "Received context: {}".format(str(context))

    print "Logging information: {}, {}".format(context.log_group_name, context.log_stream_name)
    print "Request id: {}".format(context.aws_request_id)
    print "Memory limit (MB): {}".format(context.memory_limit_in_mb)

    speech_topic_arn = os.environ['SPEECH_TOPIC_ARN']
    body = "Hello world!"
    print body

    response = {
        'statusCode': 200,
        'headers': {},
        'body': body
    }
    return response
