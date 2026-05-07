# Power BI Data Model

## Fact Table
- fact_sales

## Dimensions
- dim_product
- dim_store
- dim_customer
- dim_promotion

## Relationships
- fact_sales.product_id → dim_product.product_id
- fact_sales.store_id → dim_store.store_id
- fact_sales.customer_id → dim_customer.customer_id
- fact_sales.promo_id → dim_promotion.promo_id

## KPIs
- Total Revenue
- Average Basket Value
- Store Performance Index
- Promotion ROI
