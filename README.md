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

images uploaded to this bucket will cause an image to be indexed for detection 
`export INDEX_BUCKET=higs-index-bucket`

images uploaded to this bucket will cause the image to be searched in the collection
`export SEARCh_BUCKET=higs-search-bucket`


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
                "arn:aws:s3:::higs-bone-index",
                "arn:aws:s3:::higs-bone-search"
            ]
        },
        {
            "Sid": "Stmt1492636417000",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "logs:DescribeLogStreams"
            ],
            "Resource": [
                "arn:aws:logs:*:*:*"
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



# Lambda environment variables
SPEECH_TOPIC_ARN=arn:aws:sns:us-east-1:546275881527:higs-bone-rekognition
BONE_REK_COLLECTION=rek-bone-1
INDEX_BUCKET=higs-bone-index
SEARCH_BUCKET=higs-bone-search
    