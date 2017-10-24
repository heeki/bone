#!/bin/bash

ZIPFILE=temp/lambda.zip
ZIPINCLUDE="lambda.py scriptlets/"
LAMBDAFUNC=hackathon
LAMBDAHANDLER=lambda.lambda_handler
LAMBDAROLE=arn:aws:iam::546275881527:role/iam-role-bone-1
LAMBDAREGION=us-east-1
LAMBDARUNTIME=python2.7
LAMBDATIMEOUT=15
LAMBDAMEM=512
LAMBDALOG=temp/lambda.log

rm $ZIPFILE

aws lambda delete-function \
--region $LAMBDAREGION \
--function-name $LAMBDAFUNC

# build zip package
zip -r -x *.pyc -X $ZIPFILE $ZIPINCLUDE
unzip -vl $ZIPFILE

echo
echo Creating Lambda Function:

aws lambda create-function \
--region $LAMBDAREGION \
--function-name $LAMBDAFUNC \
--zip-file fileb://$ZIPFILE \
--role $LAMBDAROLE \
--handler $LAMBDAHANDLER \
--runtime $LAMBDARUNTIME \
--timeout $LAMBDATIMEOUT \
--memory-size $LAMBDAMEM
