#!/usr/bin/env bash

TMPPROJECTDIR=$(mktemp -d)

if [ -z $1 ]
then
    echo "Usage: $0 BUCKET"
    exit 1
else
	BUCKET=$1
fi

echo "Cloning files"
git clone https://github.com/heeki/bone.git ${TMPPROJECTDIR}/
cd ${TMPPROJECTDIR}/

echo "Zipping Files"
zip -r bone-lambda-package.zip *

echo "Uploading zip and CFN template to S3"
aws s3 cp bone-lambda-package.zip s3://${BUCKET}/bone-lambda-package.zip
aws s3 cp cloudformation/template.yaml s3://${BUCKET}/bone-template.yaml
aws s3api put-object-acl --acl public-read --bucket $BUCKET --key bone-lambda-package.zip
aws s3api put-object-acl --acl public-read --bucket $BUCKET --key bone-template.yaml

rm -rf ${TMPPROJECTDIR}

echo "Final step, deploy the CloudFormation template located at the following URL and plug in $BUCKET for the S3 bucket name parameter."
echo "https://s3.amazonaws.com/$BUCKET/bone-template.yaml" 