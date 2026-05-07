# Runbook — Operational Guide

## Pipeline Execution

1. Trigger ADF pipeline
2. Monitor Databricks job runs
3. Validate Silver layer completeness
4. Verify Gold KPI refresh

## Failure Handling

- Check Databricks logs
- Retry failed notebook task
- Validate input data in Bronze layer

## Recovery Steps

- Re-run failed task only
- If corruption → reload Bronze from Raw
