# System Design — Retail Lakehouse Platform

## Overview
End-to-end Azure-based Lakehouse architecture for retail analytics.

## Architecture Layers

### 1. Data Sources
- POS systems
- Product catalog APIs
- Store master data
- Customer systems

### 2. Ingestion Layer
- Azure Data Factory
- Batch ingestion into ADLS Gen2

### 3. Storage Layers (Medallion Architecture)
- Bronze: Raw ingested data
- Silver: Cleaned + conformed data
- Gold: Business KPIs

### 4. Processing Layer
- Azure Databricks (PySpark)
- Delta Lake for ACID transactions

### 5. Consumption Layer
- Power BI dashboards
- Analytics queries

## Key Design Patterns
- Medallion Architecture
- Star Schema modeling
- CDC (Change Data Capture)
- Batch processing (no streaming)
