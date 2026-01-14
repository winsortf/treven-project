#!/bin/bash

# Wait for LocalStack to be ready
echo "Initializing LocalStack resources..."

# Create S3 bucket
awslocal s3 mb s3://treven-data-local --region us-west-2

# Create DynamoDB table (single-table design)
awslocal dynamodb create-table \
    --table-name lon12-table \
    --attribute-definitions \
        AttributeName=PK,AttributeType=S \
        AttributeName=SK,AttributeType=S \
    --key-schema \
        AttributeName=PK,KeyType=HASH \
        AttributeName=SK,KeyType=RANGE \
    --billing-mode PAY_PER_REQUEST \
    --region us-west-2

echo "LocalStack initialization complete!"
