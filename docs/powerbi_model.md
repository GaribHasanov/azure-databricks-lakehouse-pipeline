# Power BI Semantic Model - Retail Lakehouse

## Data Sources
- gold.sales_kpis
- silver.fact_sales
- silver.dim_product
- silver.dim_store

## Relationships

fact_sales.store_id → dim_store.store_id  
fact_sales.product_id → dim_product.product_id  

## Key Measures

### Total Revenue
SUM(fact_sales.total_price)

### Total Transactions
COUNT(fact_sales.transaction_id)

### Average Basket Value
AVERAGE(fact_sales.total_price)

## Dashboards

### 1. Store Performance Dashboard
- Revenue by store
- Transactions per store
- Region comparison

### 2. Product Performance Dashboard
- Top selling products
- Category revenue share

### 3. Executive KPI Dashboard
- Total revenue
- Growth over time
- Store ranking
