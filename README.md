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

## 🔄 Data Flow
