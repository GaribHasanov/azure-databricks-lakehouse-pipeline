# Data Catalog

## Fact Tables
- fact_sales: transactional sales data (grain: 1 row per transaction line)

## Dimension Tables
- dim_product: product master data
- dim_store: store metadata
- dim_customer: customer profiles
- dim_promotion: promotion definitions

## Gold Tables
- sales_kpis: aggregated revenue and performance metrics
- store_performance: store-level KPIs
- product_performance: product-level KPIs
- promotion_effectiveness: campaign performance metrics
