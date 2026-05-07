# Data Contracts

## fact_sales
- transaction_id: STRING (NOT NULL)
- product_id: STRING (NOT NULL)
- store_id: STRING (NOT NULL)
- customer_id: STRING (NOT NULL)
- quantity: INT (> 0)
- unit_price: DOUBLE (> 0)

## Rules
- No NULL primary keys allowed
- No negative values in numeric fields
- Schema changes must be versioned
