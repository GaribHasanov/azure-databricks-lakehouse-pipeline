# Retail Lakehouse Analytics Platform

End-to-end **cloud-native data platform** built on Azure Databricks, implementing a modern **Lakehouse architecture** for retail analytics use cases.

---

## 🏗️ Architecture Overview

This project implements a **Medallion Architecture**:

- **Bronze Layer** → Raw transactional data ingestion  
- **Silver Layer** → Cleaned and structured data (Fact + Dimensions)  
- **Gold Layer** → Business KPIs and analytics datasets  

---

## 📊 Business Domain

Retail analytics platform for:

- Sales transactions analysis  
- Product performance tracking  
- Store/region performance evaluation  
- Promotion effectiveness analysis  

---

## 📁 Data Model

### Fact Table
- `fact_sales`

### Dimension Tables
- `dim_product`
- `dim_store`
- `dim_customer`
- `dim_promotion`

---

## ⚙️ Technology Stack

- Azure Databricks (PySpark)
- Azure Data Factory (Orchestration)
- Delta Lake (Storage Layer)
- Azure Data Lake Storage Gen2
- GitHub Actions (CI/CD)
- Terraform (Infrastructure as Code)
- Azure Key Vault (Secrets Management)

---



# Retail Lakehouse Analytics Platform (Azure Databricks)

## Overview
End-to-end **batch-based Lakehouse data platform** built on Azure Databricks, Azure Data Factory, and Delta Lake for retail analytics use cases.

The system implements a full **Medallion Architecture (Bronze → Silver → Gold)** with enterprise-grade data engineering patterns.

---

## 🏗️ Architecture

### Layers

- **Raw Layer**: Source data (sales, products, stores, customers, promotions)
- **Bronze Layer**: Raw ingestion into Delta tables
- **Silver Layer**: Cleaned and conformed data (Fact + Dimensions)
- **Gold Layer**: Business KPIs and analytics datasets

---

## 📊 Business Use Cases

- Sales performance analytics
- Product performance tracking
- Store-level KPIs
- Customer segmentation
- Promotion effectiveness analysis

---

## ⚙️ Technology Stack

- Azure Databricks (PySpark + Delta Lake)
- Azure Data Factory (Orchestration)
- Azure Data Lake Storage Gen2
- Terraform (Infrastructure as Code)
- GitHub Actions (CI/CD)
- Azure Key Vault (Secrets Management)
- Power BI (Reporting)

---

## 🔄 Data Flow

Raw Data → ADF Pipeline → Bronze → Databricks ETL → Silver → Gold → Power BI

---

## 📁 Project Structure

- `data/` → Raw + Bronze + Silver + Gold layers
- `adf-pipelines/` → ADF orchestration pipelines
- `databricks/` → Notebooks + Jobs
- `src/` → Core ETL + validation + observability logic
- `ci-cd/` → Terraform + GitHub Actions
- `governance/` → Data contracts, catalog, lineage
- `monitoring/` → SLA, metrics, alerts
- `docs/` → Architecture + system design + runbook

---

## 🔐 Key Features

- Medallion Architecture implementation
- Star schema data modeling
- CDC (Change Data Capture) using Delta MERGE
- Batch processing pipeline (no streaming)
- Data quality validation layer
- Observability + monitoring layer
- Infrastructure as Code (Terraform)
- CI/CD automation with GitHub Actions
- Governance framework (contracts + lineage)

---

## 📈 KPIs Generated

- Total Revenue
- Average Basket Value
- Store Performance Index
- Product Performance Ranking
- Promotion ROI

---

## 🚀 Deployment Flow

1. Terraform deploys Azure infrastructure
2. GitHub Actions triggers CI/CD pipeline
3. ADF orchestrates ingestion
4. Databricks processes Bronze → Silver → Gold
5. Power BI consumes Gold layer

---

## 📌 Notes

- This project is **batch-processing only**
- Streaming is intentionally excluded
- Designed for production-style learning and enterprise simulation

---

## 📄 Author

Data Engineering Project — Azure Lakehouse Architecture

## 🔄 Data Flow
