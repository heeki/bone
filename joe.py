
def invoke_speech(alias_name):
    """Invokes the speech engine via SNS"""
    sns = boto3.client('sns')
    sns.publish(
        TopicArn=speech_topic_arn,
        Message=JSON.dumps({'alias_name: alias_name})
    )
