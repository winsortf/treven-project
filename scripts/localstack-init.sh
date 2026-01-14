#!/bin/bash

# Wait for LocalStack to be ready
echo "Initializing LocalStack resources..."

# Create S3 bucket
awslocal s3 mb s3://treven-data-local

# Create DynamoDB tables
awslocal dynamodb create-table \
    --table-name treven-main \
    --attribute-definitions \
        AttributeName=PK,AttributeType=S \
        AttributeName=SK,AttributeType=S \
    --key-schema \
        AttributeName=PK,KeyType=HASH \
        AttributeName=SK,KeyType=RANGE \
    --billing-mode PAY_PER_REQUEST

awslocal dynamodb create-table \
    --table-name treven-audit \
    --attribute-definitions \
        AttributeName=PK,AttributeType=S \
        AttributeName=SK,AttributeType=S \
    --key-schema \
        AttributeName=PK,KeyType=HASH \
        AttributeName=SK,KeyType=RANGE \
    --billing-mode PAY_PER_REQUEST

echo "LocalStack initialization complete!"
