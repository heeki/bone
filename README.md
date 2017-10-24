# Rekognition Lambda
# Hackathon 2017


# Setup
pip install boto3

# Bucket
export BONE_S3=higs-bone-1
export BONE_IAM_POLICY=policy-bone-1
export BONE_IAM_ROLE=iam-role-bone-1


# Poilicies
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