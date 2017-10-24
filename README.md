# Rekognition Lambda
# Hackathon 2017


# Setup
pip install boto3

# Bucket
export BONE_PROFILE=1527
export BONE_REGION=us-east-1
export BONE_S3=higs-bone-1
export BONE_IAM_POLICY=policy-bone-1
export BONE_IAM_ROLE=iam-role-bone-1
export BONE_REK_COLLECTION=rek-bone-1

# Policies
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Stmt1508804824000",
            "Effect": "Allow",
            "Action": [
                "s3:*"
            ],
            "Resource": [
                "arn:aws:s3:::higs-bone-1"
            ]
        }
    ]
}
```


# Rekognition
``````
aws rekognition create-collection \
--collection-id ${BONE_REK_COLLECTION} \
--region ${BONE_REGION} \
--profile ${BONE_PROFILE}

{
    "CollectionArn": "aws:rekognition:us-east-1:546275881527:collection/rek-bone-1", 
    "StatusCode": 200
}

aws rekognition list-collections \
--region ${BONE_REGION} \
--profile ${BONE_PROFILE}

{
    "CollectionIds": [
        "rek-bone-1"
    ]
}


```


# Image locations
higs-bone-1/images/heeki.jpeg
higs-bone-1/images/joe.jpeg


# Output
```
{
    'alias_name': alias
}
```