# Carnival Consumer AI Analytics & Insights Platform

[![BigQuery](https://img.shields.io/badge/Google_BigQuery-Free_Tier-blue)](https://cloud.google.com/bigquery)
[![Looker Studio](https://img.shields.io/badge/Looker_Studio-Executive_Dashboard-orange)](https://lookerstudio.google.com)
[![Python](https://img.shields.io/badge/Python-Colab_A%2FB_Testing-green)](https://colab.research.google.com)

## Repository Overview
This repository contains the complete analytics infrastructure built to measure, analyze, and optimize Consumer AI initiatives for Carnival Cruise Line. The platform bridges raw conversational logs with executive scorecards, statistical hypothesis testing, and value realization modeling for the **SeaSmart AI Guest Assistant**.

## Technical Workflow & Architecture
```text
+-------------------------------------------------------------------------------------------------+
|                                    PROJECT PIPELINE ARCHITECTURE                                |
+------------------------+------------------------------------+-----------------------------------+
|  1. GENERATION         |  2. WAREHOUSING & ETL              |  3. STATS & VISUALIZATION         |
|  • Google Colab (CPU)  |  • Google BigQuery                 |  • Google Colab (Stats/A/B)       |
|  • Python / Pandas     |  • Project ID: driiiportfolio      |  • Looker Studio                  |
|  • Synthetic Log Data  |  • SQL Cleaning & Normalization    |  • GitHub Repository              |
+------------------------+------------------------------------+-----------------------------------+
```
---
1. **Data Generation:** `scripts/synthetic_data_generator.py` creates 10,000 interaction logs and 2,000 A/B prompt experiment records.

2. **Data Warehousing & SQL ETL:** Scripts in sql/ perform cleaning, normalization, and aggregation in BigQuery (`driiiportfolio.consumer_ai_analytics`).

3. **Statistical Modeling:** `scripts/statistical_ab_testing_analysis.py` evaluates prompt efficacy using Z-tests for proportions.

4. **Executive Dashboarding:** Dynamic Looker Studio dashboard connected to BigQuery analytical views.

### **Author**
Daniel Rodriguez III | Data Operations & Insights Professional
