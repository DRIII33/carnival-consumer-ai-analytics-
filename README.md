# Carnival Consumer AI Analytics & Insights Platform

[![BigQuery](https://img.shields.io/badge/Google_BigQuery-Free_Tier-blue)](https://cloud.google.com/bigquery)
[![Looker Studio](https://img.shields.io/badge/Looker_Studio-Executive_Dashboard-orange)](https://lookerstudio.google.com)
[![Python](https://img.shields.io/badge/Python-Colab_A%2FB_Testing-green)](https://colab.research.google.com)

## Repository Overview
This repository contains the end-to-end analytics infrastructure built to measure, analyze, and optimize Consumer AI initiatives for Carnival Cruise Line[cite: 2]. The platform bridges raw conversational logs with executive scorecards, statistical hypothesis testing, and value realization modeling.

## Technical Workflow
1. **Data Generation:** `scripts/synthetic_data_generator.py` generates realistic interaction logs and A/B test parameters.
2. **Data Warehousing:** SQL scripts in `sql/` perform cleaning, normalization, and aggregation within BigQuery project `driiiportfolio`.
3. **Statistical Analysis:** `scripts/statistical_ab_testing_analysis.py` evaluates prompt efficacy using Z-test hypothesis testing.
4. **Visualization:** Executive scorecard hosted on Looker Studio tracking KPIs and intent performance.

## Author
**Daniel Rodriguez III** | Data Operations & Insights Professional[cite: 2]
