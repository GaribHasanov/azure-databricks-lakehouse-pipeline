# Retail Lakehouse Analytics Platform

End-to-end **cloud-native batch data platform** built on Azure Databricks implementing a modern **Lakehouse architecture** for retail analytics use cases.

---

## 🏗️ Architecture Overview

This project implements a **Medallion Architecture**:

- **Bronze Layer** → Raw transactional data ingestion (ADF → ADLS)
- **Silver Layer** → Cleaned and structured data (Fact + Dimensions via Databricks)
- **Gold Layer** → Business KPIs and analytics datasets

---

## 🔄 Data Flow

Raw Data Sources  
→ Azure Data Factory (Orchestration)  
→ Bronze Layer (Delta Lake)  
→ Databricks ETL (PySpark)  
→ Silver Layer (Fact & Dimension Tables)  
→ Gold Layer (Business KPIs)  
→ Power BI / Analytics

---

## 📊 Business Domain

Retail analytics platform covering:

- Sales transactions analysis  
- Product performance tracking  
- Store/region performance evaluation  
- Promotion effectiveness analysis  
- Customer segmentation  

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

## 📊 KPIs Generated

- Total Revenue  
- Average Basket Value  
- Store Performance Index  
- Product Sales Ranking  
- Promotion ROI  
- Customer Segmentation Metrics  

---

## ⚙️ Key Engineering Features

- Medallion Architecture (Bronze / Silver / Gold)
- Star Schema Data Modeling
- CDC (Change Data Capture) using Delta MERGE
- Batch Processing Pipeline (no streaming)
- Data Quality Validation Layer
- Observability & Monitoring Layer
- Infrastructure as Code (Terraform)
- CI/CD automation (GitHub Actions)

---

## 🧱 Repository Structure

- `data/` → Raw, Bronze, Silver, Gold layers
- `adf-pipelines/` → Azure Data Factory orchestration
- `databricks/` → Notebooks and job definitions
- `src/` → ETL, validation, observability, utils
- `ci-cd/` → Terraform + GitHub Actions
- `governance/` → Data contracts, lineage, catalog
- `monitoring/` → SLAs, metrics, alerts
- `docs/` → Architecture, system design, runbooks

---

## 🚀 Deployment Flow

1. Terraform provisions Azure infrastructure (ADLS, ADF, Databricks, Key Vault)
2. GitHub Actions runs CI/CD pipeline
3. Azure Data Factory orchestrates ingestion workflows
4. Databricks processes Bronze → Silver → Gold layers
5. Power BI consumes Gold layer for reporting

---

## 🔐 Production Principles

This project follows production-grade data engineering principles including:

- Medallion Architecture
- Data Contracts & Governance
- Idempotent ETL design
- CDC-based incremental processing
- Observability & SLA monitoring
- Infrastructure as Code (IaC)

---

## 📌 Notes

- Batch processing only (no streaming)
- Designed for enterprise-style analytics workloads
- Fully modular and scalable architecture

---

## 📈 Outcome

This project simulates a real-world **Azure Data Engineering platform** used for retail analytics at scale.
