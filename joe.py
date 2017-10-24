

# .. receive "event" from lambda handler
try:
    for record in event['Records']:
        s3_bucket = record['s3']['bucket']['name']
        image_key = record['s3']['object']['key']
except KeyError as ke:
    print("Input object is not formatted correctly. Error: %s", str(ke))

def invoke_speech(alias_name):
    """Invokes the speech engine via SNS"""
    sns = boto3.client('sns')
    sns.publish(
        TopicArn=speech_topic_arn,
        Message=JSON.dumps({'alias_name: alias_name})
    )
