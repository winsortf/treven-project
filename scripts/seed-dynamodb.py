#!/usr/bin/env python3
"""Seed DynamoDB with initial data from hackathon dataset."""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

import boto3
from botocore.config import Config

# Configuration
TABLE_NAME = os.getenv("DYNAMODB_TABLE", "lon12-table")
REGION = os.getenv("AWS_REGION", "us-west-2")
ENDPOINT_URL = os.getenv("DYNAMODB_ENDPOINT", None)

# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent
DATASET_DIR = PROJECT_ROOT / "dataset_for_hackathon" / "AWS-Hackathon-2026-Dataset"


def get_dynamodb_client():
    """Create DynamoDB client."""
    config = Config(region_name=REGION)
    if ENDPOINT_URL:
        return boto3.client("dynamodb", endpoint_url=ENDPOINT_URL, config=config)
    return boto3.client("dynamodb", config=config)


def put_item(client, item: dict):
    """Put an item into DynamoDB."""
    dynamo_item = {}
    for key, value in item.items():
        if value is None:
            continue
        if isinstance(value, str):
            dynamo_item[key] = {"S": value}
        elif isinstance(value, bool):
            dynamo_item[key] = {"BOOL": value}
        elif isinstance(value, int):
            dynamo_item[key] = {"N": str(value)}
        elif isinstance(value, float):
            dynamo_item[key] = {"N": str(value)}
        elif isinstance(value, list):
            dynamo_item[key] = {"S": json.dumps(value)}
        elif isinstance(value, dict):
            dynamo_item[key] = {"S": json.dumps(value)}

    client.put_item(TableName=TABLE_NAME, Item=dynamo_item)


def seed_partners(client):
    """Seed partner organizations."""
    print("Seeding partners...")
    partners = [
        {"id": "partner-001", "name": "Barclays Bank", "partner_type": "fi", "reports_shared": 12, "access_level": "download"},
        {"id": "partner-002", "name": "HSBC", "partner_type": "fi", "reports_shared": 8, "access_level": "view"},
        {"id": "partner-003", "name": "Anti-Slavery International", "partner_type": "ngo", "reports_shared": 15, "access_level": "download"},
        {"id": "partner-004", "name": "Metropolitan Police", "partner_type": "le", "reports_shared": 6, "access_level": "download"},
        {"id": "partner-005", "name": "Europol", "partner_type": "le", "reports_shared": 4, "access_level": "view"},
        {"id": "partner-006", "name": "Standard Chartered", "partner_type": "fi", "reports_shared": 10, "access_level": "download"},
        {"id": "partner-007", "name": "IOM", "partner_type": "ngo", "reports_shared": 22, "access_level": "download"},
        {"id": "partner-008", "name": "UNODC", "partner_type": "ngo", "reports_shared": 18, "access_level": "view"},
    ]

    for partner in partners:
        item = {
            "PK": "PARTNERS",
            "SK": f"PARTNER#{partner['id']}",
            "entityType": "Partner",
            "id": partner["id"],
            "name": partner["name"],
            "type": partner["partner_type"],
            "reportsShared": partner["reports_shared"],
            "accessLevel": partner["access_level"],
            "createdAt": datetime.utcnow().isoformat() + "Z",
        }
        put_item(client, item)

    print(f"  Created {len(partners)} partners")


def seed_trends(client):
    """Seed trends data."""
    print("Seeding trends...")
    trends = [
        {
            "id": "trend-001",
            "country": "United Kingdom",
            "countryCode": "GB",
            "title": "Modern Slavery in Supply Chains",
            "confidence": "high",
            "exploitationType": "labour_exploitation",
            "summary": "Increasing evidence of labour exploitation in UK supply chains, particularly in car washes, agriculture, and construction sectors.",
        },
        {
            "id": "trend-002",
            "country": "India",
            "countryCode": "IN",
            "title": "Child Labour in Manufacturing",
            "confidence": "high",
            "exploitationType": "child_labour",
            "summary": "Persistent child labour issues in garment manufacturing and brick kilns, often linked to debt bondage.",
        },
        {
            "id": "trend-003",
            "country": "Brazil",
            "countryCode": "BR",
            "title": "Sexual Exploitation in Tourism",
            "confidence": "medium",
            "exploitationType": "sexual_exploitation",
            "summary": "Growing concern about sexual exploitation linked to tourism industry in coastal areas.",
        },
        {
            "id": "trend-004",
            "country": "Nigeria",
            "countryCode": "NG",
            "title": "Trafficking to Europe",
            "confidence": "high",
            "exploitationType": "sexual_exploitation",
            "summary": "Well-documented trafficking routes from Nigeria to Europe, particularly Italy and Spain.",
        },
        {
            "id": "trend-005",
            "country": "Philippines",
            "countryCode": "PH",
            "title": "Online Sexual Exploitation",
            "confidence": "high",
            "exploitationType": "sexual_exploitation",
            "summary": "Increasing online sexual exploitation of children, often facilitated by family members.",
        },
        {
            "id": "trend-006",
            "country": "Pakistan",
            "countryCode": "PK",
            "title": "Bonded Labour in Brick Kilns",
            "confidence": "high",
            "exploitationType": "labour_exploitation",
            "summary": "Generational debt bondage in brick kiln industry affecting entire families.",
        },
    ]

    sources = [
        {"id": "src-001", "url": "https://www.gov.uk/tip-report", "title": "UK Modern Slavery Report 2025", "publisher": "UK Government", "trustScore": 95},
        {"id": "src-002", "url": "https://www.ilo.org/reports", "title": "ILO Global Estimates of Modern Slavery", "publisher": "ILO", "trustScore": 98},
    ]

    for trend in trends:
        item = {
            "PK": "TRENDS",
            "SK": f"TREND#{trend['countryCode']}#{trend['id']}",
            "entityType": "Trend",
            "id": trend["id"],
            "country": trend["country"],
            "countryCode": trend["countryCode"],
            "title": trend["title"],
            "confidence": trend["confidence"],
            "exploitationType": trend["exploitationType"],
            "summary": trend["summary"],
            "sources": json.dumps(sources[:2]),
            "lastUpdated": datetime.utcnow().isoformat() + "Z",
        }
        put_item(client, item)

    print(f"  Created {len(trends)} trends")


def seed_reports(client):
    """Seed sample reports."""
    print("Seeding reports...")
    org_id = "stt"

    reports = [
        {
            "id": "report-001",
            "title": "Labour Exploitation in UK Car Washes",
            "country": "United Kingdom",
            "sector": "Car Wash",
            "exploitationType": "labour_exploitation",
            "status": "approved",
            "version": 3,
            "wordCount": 2450,
        },
        {
            "id": "report-002",
            "title": "Sexual Exploitation via Online Platforms in Italy",
            "country": "Italy",
            "sector": "Online Platforms",
            "exploitationType": "sexual_exploitation",
            "status": "in_review",
            "version": 2,
            "wordCount": 2180,
        },
        {
            "id": "report-003",
            "title": "Child Labour in Indian Manufacturing",
            "country": "India",
            "sector": "Manufacturing",
            "exploitationType": "child_labour",
            "status": "draft",
            "version": 1,
            "wordCount": 1850,
        },
        {
            "id": "report-004",
            "title": "Trafficking Routes from Nigeria to Europe",
            "country": "Nigeria",
            "sector": "Cross-border",
            "exploitationType": "sexual_exploitation",
            "status": "approved",
            "version": 4,
            "wordCount": 3200,
        },
    ]

    for report in reports:
        now = datetime.utcnow().isoformat() + "Z"
        item = {
            "PK": f"ORG#{org_id}",
            "SK": f"REPORT#{report['id']}",
            "entityType": "Report",
            "id": report["id"],
            "orgId": org_id,
            "title": report["title"],
            "country": report["country"],
            "sector": report["sector"],
            "exploitationType": report["exploitationType"],
            "status": report["status"],
            "version": report["version"],
            "wordCount": report["wordCount"],
            "createdAt": now,
            "updatedAt": now,
        }
        put_item(client, item)

    print(f"  Created {len(reports)} reports")


def seed_tah_articles(client, limit: int = 100):
    """Seed TAH articles from synthetic dataset."""
    print("Seeding TAH articles from synthetic dataset...")

    dataset_file = DATASET_DIR / "synthetic_tah_dataset.jsonl"
    if not dataset_file.exists():
        print(f"  Warning: Dataset file not found: {dataset_file}")
        return

    count = 0
    with open(dataset_file, "r") as f:
        for line in f:
            if count >= limit:
                break

            try:
                article = json.loads(line.strip())

                # Extract region
                region = article.get("region", "GLOBAL")
                if not region:
                    region = "GLOBAL"

                # Create TAH article item
                doc_id = article.get("doc_id", f"synth-{count}")

                item = {
                    "PK": f"TAH#{region.upper().replace(' ', '_').replace('-', '_')}",
                    "SK": f"ARTICLE#{doc_id}",
                    "entityType": "TahArticle",
                    "docId": doc_id,
                    "title": article.get("title", "Untitled"),
                    "article": article.get("article", "")[:5000],  # Truncate long articles
                    "summary": article.get("summary", "")[:2000] if article.get("summary") else None,
                    "region": region,
                    "sourceType": article.get("source_type"),
                    "trfkType": json.dumps(article.get("trfk_type")) if article.get("trfk_type") else None,
                    "trfkSubtype": json.dumps(article.get("trfk_subtype")) if article.get("trfk_subtype") else None,
                    "recruitment": json.dumps(article.get("recruitment")) if article.get("recruitment") else None,
                    "coercion": json.dumps(article.get("coercion")) if article.get("coercion") else None,
                    "crawlDate": article.get("crawl_date"),
                }

                put_item(client, item)
                count += 1

            except json.JSONDecodeError:
                continue

    print(f"  Created {count} TAH articles")


def seed_india_labour_articles(client, limit: int = 50):
    """Seed India labour exploitation articles."""
    print("Seeding India labour articles...")

    dataset_file = DATASET_DIR / "tah-labour-india-six-months.json"
    if not dataset_file.exists():
        print(f"  Warning: Dataset file not found: {dataset_file}")
        return

    with open(dataset_file, "r") as f:
        articles = json.load(f)

    count = 0
    for article in articles[:limit]:
        try:
            doc_id = article.get("_id", {}).get("$oid", f"india-{count}")

            item = {
                "PK": "TAH#ASIA_PACIFIC",
                "SK": f"ARTICLE#{doc_id}",
                "entityType": "TahArticle",
                "docId": doc_id,
                "url": article.get("url"),
                "title": article.get("title", "Untitled"),
                "article": article.get("article", "")[:5000],
                "summary": article.get("summary", "")[:2000] if article.get("summary") else None,
                "region": "Asia-Pacific",
                "sourceType": "NEWS",
                "trfkType": json.dumps(article.get("trfk_type")) if article.get("trfk_type") else None,
                "trfkSubtype": json.dumps(article.get("trfk_subtype")) if article.get("trfk_subtype") else None,
                "recruitment": json.dumps(article.get("recruitment")) if article.get("recruitment") else None,
                "coercion": json.dumps(article.get("coercion")) if article.get("coercion") else None,
                "crawlDate": article.get("crawl_date"),
                "publishDate": article.get("publish_date"),
            }

            put_item(client, item)
            count += 1

        except Exception as e:
            print(f"  Error processing article: {e}")
            continue

    print(f"  Created {count} India labour articles")


def seed_india_se_articles(client, limit: int = 50):
    """Seed India sexual exploitation articles."""
    print("Seeding India SE articles...")

    dataset_file = DATASET_DIR / "tah-se-india-six-months.json"
    if not dataset_file.exists():
        print(f"  Warning: Dataset file not found: {dataset_file}")
        return

    with open(dataset_file, "r") as f:
        articles = json.load(f)

    count = 0
    for article in articles[:limit]:
        try:
            doc_id = article.get("_id", {}).get("$oid", f"india-se-{count}")

            item = {
                "PK": "TAH#ASIA_PACIFIC",
                "SK": f"ARTICLE#{doc_id}",
                "entityType": "TahArticle",
                "docId": doc_id,
                "url": article.get("url"),
                "title": article.get("title", "Untitled"),
                "article": article.get("article", "")[:5000],
                "summary": article.get("summary", "")[:2000] if article.get("summary") else None,
                "region": "Asia-Pacific",
                "sourceType": "NEWS",
                "trfkType": json.dumps(article.get("trfk_type")) if article.get("trfk_type") else None,
                "trfkSubtype": json.dumps(article.get("trfk_subtype")) if article.get("trfk_subtype") else None,
                "recruitment": json.dumps(article.get("recruitment")) if article.get("recruitment") else None,
                "coercion": json.dumps(article.get("coercion")) if article.get("coercion") else None,
                "crawlDate": article.get("crawl_date"),
                "publishDate": article.get("publish_date"),
            }

            put_item(client, item)
            count += 1

        except Exception as e:
            print(f"  Error processing article: {e}")
            continue

    print(f"  Created {count} India SE articles")


def main():
    """Main entry point."""
    print(f"Seeding DynamoDB table: {TABLE_NAME}")
    print(f"Region: {REGION}")
    if ENDPOINT_URL:
        print(f"Endpoint: {ENDPOINT_URL}")
    print()

    client = get_dynamodb_client()

    # Seed all data
    seed_partners(client)
    seed_trends(client)
    seed_reports(client)
    seed_tah_articles(client, limit=100)
    seed_india_labour_articles(client, limit=100)
    seed_india_se_articles(client, limit=100)

    print()
    print("Seeding complete!")
    print(f"  Total: Partners, Trends, Reports, and ~300 TAH articles loaded")


if __name__ == "__main__":
    main()
