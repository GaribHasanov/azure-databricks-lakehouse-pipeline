# SLA Definitions

## Data Pipelines

- Bronze ingestion: max 30 minutes latency
- Silver transformation: max 1 hour latency
- Gold KPIs: max 2 hours latency

## Availability
- 99.5% pipeline success rate monthly

## Failure Handling
- Any failure triggers retry (max 3 attempts)
- After 3 failures → alert triggered
