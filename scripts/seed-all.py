#!/usr/bin/env python3
"""Comprehensive seed script - loads all data into DynamoDB."""

import json
import os
from pathlib import Path

import boto3
from botocore.config import Config

# Configuration
TABLE_NAME = os.getenv("DYNAMODB_TABLE", "lon12-table")
REGION = os.getenv("AWS_REGION", "us-west-2")
ENDPOINT_URL = os.getenv("DYNAMODB_ENDPOINT", "http://localhost:4566")

# Paths
SCRIPT_DIR = Path(__file__).parent
SEED_DATA_DIR = SCRIPT_DIR / "seed-data"


def get_dynamodb_client():
    """Create DynamoDB client."""
    config = Config(region_name=REGION)
    return boto3.client("dynamodb", endpoint_url=ENDPOINT_URL, config=config)


def load_json_file(filename: str) -> list:
    """Load items from a JSON file."""
    filepath = SEED_DATA_DIR / filename
    if not filepath.exists():
        print(f"  Warning: {filepath} not found")
        return []
    with open(filepath, "r") as f:
        return json.load(f)


def batch_write_items(client, items: list, entity_type: str):
    """Write items to DynamoDB in batches of 25."""
    if not items:
        return 0

    count = 0
    batch = []

    for item in items:
        batch.append({"PutRequest": {"Item": item}})
        count += 1

        if len(batch) == 25:
            client.batch_write_item(RequestItems={TABLE_NAME: batch})
            batch = []

    if batch:
        client.batch_write_item(RequestItems={TABLE_NAME: batch})

    print(f"  Loaded {count} {entity_type}")
    return count


def seed_from_files(client):
    """Load seed data from JSON files."""
    print("Loading seed data from files...")

    total = 0

    # Load each entity type
    files = [
        ("partners.json", "Partners"),
        ("trends.json", "Trends"),
        ("reports.json", "Reports"),
        ("conversations.json", "Conversations"),
        ("messages.json", "Messages"),
    ]

    for filename, entity_type in files:
        items = load_json_file(filename)
        total += batch_write_items(client, items, entity_type)

    return total


def seed_hardcoded_partners(client):
    """Seed partners if no JSON file exists."""
    partners = [
        {
            "PK": {"S": "PARTNERS"},
            "SK": {"S": "PARTNER#partner-001"},
            "entityType": {"S": "Partner"},
            "id": {"S": "partner-001"},
            "name": {"S": "Barclays Bank"},
            "type": {"S": "fi"},
            "reportsShared": {"N": "12"},
            "accessLevel": {"S": "download"},
            "createdAt": {"S": "2026-01-10T10:00:00Z"},
        },
        {
            "PK": {"S": "PARTNERS"},
            "SK": {"S": "PARTNER#partner-002"},
            "entityType": {"S": "Partner"},
            "id": {"S": "partner-002"},
            "name": {"S": "HSBC"},
            "type": {"S": "fi"},
            "reportsShared": {"N": "8"},
            "accessLevel": {"S": "view"},
            "createdAt": {"S": "2026-01-08T09:00:00Z"},
        },
        {
            "PK": {"S": "PARTNERS"},
            "SK": {"S": "PARTNER#partner-003"},
            "entityType": {"S": "Partner"},
            "id": {"S": "partner-003"},
            "name": {"S": "Anti-Slavery International"},
            "type": {"S": "ngo"},
            "reportsShared": {"N": "15"},
            "accessLevel": {"S": "download"},
            "createdAt": {"S": "2026-01-05T11:00:00Z"},
        },
        {
            "PK": {"S": "PARTNERS"},
            "SK": {"S": "PARTNER#partner-004"},
            "entityType": {"S": "Partner"},
            "id": {"S": "partner-004"},
            "name": {"S": "Metropolitan Police"},
            "type": {"S": "le"},
            "reportsShared": {"N": "6"},
            "accessLevel": {"S": "download"},
            "createdAt": {"S": "2026-01-12T14:30:00Z"},
        },
        {
            "PK": {"S": "PARTNERS"},
            "SK": {"S": "PARTNER#partner-005"},
            "entityType": {"S": "Partner"},
            "id": {"S": "partner-005"},
            "name": {"S": "Europol"},
            "type": {"S": "le"},
            "reportsShared": {"N": "4"},
            "accessLevel": {"S": "view"},
            "createdAt": {"S": "2026-01-11T16:00:00Z"},
        },
        {
            "PK": {"S": "PARTNERS"},
            "SK": {"S": "PARTNER#partner-006"},
            "entityType": {"S": "Partner"},
            "id": {"S": "partner-006"},
            "name": {"S": "Standard Chartered"},
            "type": {"S": "fi"},
            "reportsShared": {"N": "10"},
            "accessLevel": {"S": "download"},
            "createdAt": {"S": "2026-01-09T08:00:00Z"},
        },
    ]
    return batch_write_items(client, partners, "Partners (hardcoded)")


def seed_hardcoded_trends(client):
    """Seed trends if no JSON file exists."""
    trends = [
        {
            "PK": {"S": "TRENDS"},
            "SK": {"S": "TREND#GB#trend-001"},
            "entityType": {"S": "Trend"},
            "id": {"S": "trend-001"},
            "country": {"S": "United Kingdom"},
            "countryCode": {"S": "GB"},
            "title": {"S": "Modern Slavery in Supply Chains"},
            "confidence": {"S": "high"},
            "exploitationType": {"S": "labour_exploitation"},
            "summary": {"S": "Increasing evidence of labour exploitation in UK supply chains, particularly in car washes, agriculture, and construction sectors."},
            "sources": {"S": "[]"},
            "lastUpdated": {"S": "2026-01-15T00:00:00Z"},
        },
        {
            "PK": {"S": "TRENDS"},
            "SK": {"S": "TREND#IN#trend-002"},
            "entityType": {"S": "Trend"},
            "id": {"S": "trend-002"},
            "country": {"S": "India"},
            "countryCode": {"S": "IN"},
            "title": {"S": "Child Labour in Manufacturing"},
            "confidence": {"S": "high"},
            "exploitationType": {"S": "child_labour"},
            "summary": {"S": "Persistent child labour issues in garment manufacturing and brick kilns, often linked to debt bondage."},
            "sources": {"S": "[]"},
            "lastUpdated": {"S": "2026-01-15T00:00:00Z"},
        },
        {
            "PK": {"S": "TRENDS"},
            "SK": {"S": "TREND#BR#trend-003"},
            "entityType": {"S": "Trend"},
            "id": {"S": "trend-003"},
            "country": {"S": "Brazil"},
            "countryCode": {"S": "BR"},
            "title": {"S": "Sexual Exploitation in Tourism"},
            "confidence": {"S": "medium"},
            "exploitationType": {"S": "sexual_exploitation"},
            "summary": {"S": "Growing concern about sexual exploitation linked to tourism industry in coastal areas."},
            "sources": {"S": "[]"},
            "lastUpdated": {"S": "2026-01-15T00:00:00Z"},
        },
    ]
    return batch_write_items(client, trends, "Trends (hardcoded)")


def seed_hardcoded_reports(client):
    """Seed reports if no JSON file exists."""
    reports = [
        {
            "PK": {"S": "ORG#stt"},
            "SK": {"S": "REPORT#report-001"},
            "entityType": {"S": "Report"},
            "id": {"S": "report-001"},
            "orgId": {"S": "stt"},
            "title": {"S": "Labour Exploitation in UK Car Washes"},
            "country": {"S": "United Kingdom"},
            "sector": {"S": "Car Wash"},
            "exploitationType": {"S": "labour_exploitation"},
            "status": {"S": "approved"},
            "version": {"N": "3"},
            "wordCount": {"N": "2450"},
            "createdAt": {"S": "2026-01-10T10:00:00Z"},
            "updatedAt": {"S": "2026-01-12T14:30:00Z"},
        },
        {
            "PK": {"S": "ORG#stt"},
            "SK": {"S": "REPORT#report-002"},
            "entityType": {"S": "Report"},
            "id": {"S": "report-002"},
            "orgId": {"S": "stt"},
            "title": {"S": "Sexual Exploitation via Online Platforms in Italy"},
            "country": {"S": "Italy"},
            "sector": {"S": "Online Platforms"},
            "exploitationType": {"S": "sexual_exploitation"},
            "status": {"S": "in_review"},
            "version": {"N": "2"},
            "wordCount": {"N": "2180"},
            "createdAt": {"S": "2026-01-08T09:00:00Z"},
            "updatedAt": {"S": "2026-01-11T16:00:00Z"},
        },
        {
            "PK": {"S": "ORG#stt"},
            "SK": {"S": "REPORT#report-003"},
            "entityType": {"S": "Report"},
            "id": {"S": "report-003"},
            "orgId": {"S": "stt"},
            "title": {"S": "Child Labour in Indian Manufacturing"},
            "country": {"S": "India"},
            "sector": {"S": "Manufacturing"},
            "exploitationType": {"S": "child_labour"},
            "status": {"S": "draft"},
            "version": {"N": "1"},
            "wordCount": {"N": "1850"},
            "createdAt": {"S": "2026-01-05T11:00:00Z"},
            "updatedAt": {"S": "2026-01-05T11:00:00Z"},
        },
    ]
    return batch_write_items(client, reports, "Reports (hardcoded)")


def main():
    """Main entry point."""
    print(f"=== Comprehensive DynamoDB Seed ===")
    print(f"Table: {TABLE_NAME}")
    print(f"Region: {REGION}")
    print(f"Endpoint: {ENDPOINT_URL}")
    print()

    client = get_dynamodb_client()

    # Check if seed-data directory exists with files
    if SEED_DATA_DIR.exists() and (SEED_DATA_DIR / "partners.json").exists():
        total = seed_from_files(client)
    else:
        print("No seed-data files found, using hardcoded data...")
        total = 0
        total += seed_hardcoded_partners(client)
        total += seed_hardcoded_trends(client)
        total += seed_hardcoded_reports(client)

    print()
    print(f"=== Seeding complete! Total items: {total} ===")


if __name__ == "__main__":
    main()
