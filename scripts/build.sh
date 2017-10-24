#!/usr/bin/env bash
cd $CODEBUILD_SRC_DIR

echo "Zipping Files"
zip -r bone-lambda-package.zip *

echo "Uploading zip and CFN template to S3"
set VERSION=`$CODEBUILD_SOURCE_VERSION | cut -c1-8`
aws s3 cp bone-lambda-package.zip s3://${OUTPUT_BUCKET}/bone-lambda-package-$VERSION.zip
aws s3 cp cloudformation/template.yaml s3://${OUTPUT_BUCKET}/template.yaml
aws s3api put-object-acl --acl public-read --bucket $OUTPUT_BUCKET --key bone-lambda-package-$VERSION.zip
aws s3api put-object-acl --acl public-read --bucket $OUTPUT_BUCKET --key template.yaml

echo "ZIP FILE --> https://s3.amazonaws.com/$OUTPUT_BUCKET/bone-lambda-package-$VERSION.zip"
echo "YML FILE --> https://s3.amazonaws.com/$OUTPUT_BUCKET/template.yaml"
