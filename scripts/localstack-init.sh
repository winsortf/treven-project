#!/bin/bash

# Wait for LocalStack to be ready
echo "Initializing LocalStack resources..."

# Create S3 buckets
awslocal s3 mb s3://lon12-bucket --region us-west-2
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

echo "Waiting for table to be active..."
awslocal dynamodb wait table-exists --table-name lon12-table --region us-west-2
sleep 2

echo "LocalStack table created!"

# Seed initial data
echo "Seeding initial data..."

# Partners
awslocal dynamodb put-item --table-name lon12-table --item '{"PK":{"S":"PARTNERS"},"SK":{"S":"PARTNER#partner-001"},"entityType":{"S":"Partner"},"id":{"S":"partner-001"},"name":{"S":"Barclays Bank"},"type":{"S":"fi"},"reportsShared":{"N":"12"},"accessLevel":{"S":"download"},"createdAt":{"S":"2026-01-10T10:00:00Z"}}'
awslocal dynamodb put-item --table-name lon12-table --item '{"PK":{"S":"PARTNERS"},"SK":{"S":"PARTNER#partner-002"},"entityType":{"S":"Partner"},"id":{"S":"partner-002"},"name":{"S":"HSBC"},"type":{"S":"fi"},"reportsShared":{"N":"8"},"accessLevel":{"S":"view"},"createdAt":{"S":"2026-01-08T09:00:00Z"}}'
awslocal dynamodb put-item --table-name lon12-table --item '{"PK":{"S":"PARTNERS"},"SK":{"S":"PARTNER#partner-003"},"entityType":{"S":"Partner"},"id":{"S":"partner-003"},"name":{"S":"Anti-Slavery International"},"type":{"S":"ngo"},"reportsShared":{"N":"15"},"accessLevel":{"S":"download"},"createdAt":{"S":"2026-01-05T11:00:00Z"}}'
awslocal dynamodb put-item --table-name lon12-table --item '{"PK":{"S":"PARTNERS"},"SK":{"S":"PARTNER#partner-004"},"entityType":{"S":"Partner"},"id":{"S":"partner-004"},"name":{"S":"Metropolitan Police"},"type":{"S":"le"},"reportsShared":{"N":"6"},"accessLevel":{"S":"download"},"createdAt":{"S":"2026-01-12T14:30:00Z"}}'
awslocal dynamodb put-item --table-name lon12-table --item '{"PK":{"S":"PARTNERS"},"SK":{"S":"PARTNER#partner-005"},"entityType":{"S":"Partner"},"id":{"S":"partner-005"},"name":{"S":"Europol"},"type":{"S":"le"},"reportsShared":{"N":"4"},"accessLevel":{"S":"view"},"createdAt":{"S":"2026-01-11T16:00:00Z"}}'
awslocal dynamodb put-item --table-name lon12-table --item '{"PK":{"S":"PARTNERS"},"SK":{"S":"PARTNER#partner-006"},"entityType":{"S":"Partner"},"id":{"S":"partner-006"},"name":{"S":"Standard Chartered"},"type":{"S":"fi"},"reportsShared":{"N":"10"},"accessLevel":{"S":"download"},"createdAt":{"S":"2026-01-09T08:00:00Z"}}'

# Trends
awslocal dynamodb put-item --table-name lon12-table --item '{"PK":{"S":"TRENDS"},"SK":{"S":"TREND#GB#trend-001"},"entityType":{"S":"Trend"},"id":{"S":"trend-001"},"country":{"S":"United Kingdom"},"countryCode":{"S":"GB"},"title":{"S":"Modern Slavery in Supply Chains"},"confidence":{"S":"high"},"exploitationType":{"S":"labour_exploitation"},"summary":{"S":"Increasing evidence of labour exploitation in UK supply chains, particularly in car washes, agriculture, and construction sectors."},"sources":{"S":"[]"},"lastUpdated":{"S":"2026-01-15T00:00:00Z"}}'
awslocal dynamodb put-item --table-name lon12-table --item '{"PK":{"S":"TRENDS"},"SK":{"S":"TREND#IN#trend-002"},"entityType":{"S":"Trend"},"id":{"S":"trend-002"},"country":{"S":"India"},"countryCode":{"S":"IN"},"title":{"S":"Child Labour in Manufacturing"},"confidence":{"S":"high"},"exploitationType":{"S":"child_labour"},"summary":{"S":"Persistent child labour issues in garment manufacturing and brick kilns, often linked to debt bondage."},"sources":{"S":"[]"},"lastUpdated":{"S":"2026-01-15T00:00:00Z"}}'
awslocal dynamodb put-item --table-name lon12-table --item '{"PK":{"S":"TRENDS"},"SK":{"S":"TREND#BR#trend-003"},"entityType":{"S":"Trend"},"id":{"S":"trend-003"},"country":{"S":"Brazil"},"countryCode":{"S":"BR"},"title":{"S":"Sexual Exploitation in Tourism"},"confidence":{"S":"medium"},"exploitationType":{"S":"sexual_exploitation"},"summary":{"S":"Growing concern about sexual exploitation linked to tourism industry in coastal areas."},"sources":{"S":"[]"},"lastUpdated":{"S":"2026-01-15T00:00:00Z"}}'

# Reports
awslocal dynamodb put-item --table-name lon12-table --item '{"PK":{"S":"ORG#stt"},"SK":{"S":"REPORT#report-001"},"entityType":{"S":"Report"},"id":{"S":"report-001"},"orgId":{"S":"stt"},"title":{"S":"Labour Exploitation in UK Car Washes"},"country":{"S":"United Kingdom"},"sector":{"S":"Car Wash"},"exploitationType":{"S":"labour_exploitation"},"status":{"S":"approved"},"version":{"N":"3"},"wordCount":{"N":"2450"},"createdAt":{"S":"2026-01-10T10:00:00Z"},"updatedAt":{"S":"2026-01-12T14:30:00Z"}}'
awslocal dynamodb put-item --table-name lon12-table --item '{"PK":{"S":"ORG#stt"},"SK":{"S":"REPORT#report-002"},"entityType":{"S":"Report"},"id":{"S":"report-002"},"orgId":{"S":"stt"},"title":{"S":"Sexual Exploitation via Online Platforms in Italy"},"country":{"S":"Italy"},"sector":{"S":"Online Platforms"},"exploitationType":{"S":"sexual_exploitation"},"status":{"S":"in_review"},"version":{"N":"2"},"wordCount":{"N":"2180"},"createdAt":{"S":"2026-01-08T09:00:00Z"},"updatedAt":{"S":"2026-01-11T16:00:00Z"}}'
awslocal dynamodb put-item --table-name lon12-table --item '{"PK":{"S":"ORG#stt"},"SK":{"S":"REPORT#report-003"},"entityType":{"S":"Report"},"id":{"S":"report-003"},"orgId":{"S":"stt"},"title":{"S":"Child Labour in Indian Manufacturing"},"country":{"S":"India"},"sector":{"S":"Manufacturing"},"exploitationType":{"S":"child_labour"},"status":{"S":"draft"},"version":{"N":"1"},"wordCount":{"N":"1850"},"createdAt":{"S":"2026-01-05T11:00:00Z"},"updatedAt":{"S":"2026-01-05T11:00:00Z"}}'

echo "LocalStack initialization complete!"
