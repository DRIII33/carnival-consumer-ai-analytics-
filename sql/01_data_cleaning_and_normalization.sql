-- File: sql/01_data_cleaning_and_normalization.sql
-- Description: Cleans raw AI interaction logs, standardizes timestamps, and creates staging view.

CREATE OR REPLACE VIEW `driiiportfolio.consumer_ai_analytics.vw_stg_ai_logs` AS
SELECT
  session_id,
  guest_id,
  TIMESTAMP(interaction_timestamp) AS interaction_timestamp,
  DATE(interaction_timestamp) AS interaction_date,
  LOWER(channel) AS channel,
  intent_category,
  turn_count,
  sentiment_score,
  CASE
    WHEN sentiment_score >= 0.35 THEN 'Positive'
    WHEN sentiment_score <= -0.20 THEN 'Negative'
    ELSE 'Neutral'
  END AS sentiment_tier,
  CAST(is_contained AS INT64) AS is_contained,
  CAST(is_escalated AS INT64) AS is_escalated,
  ROUND(CAST(estimated_cost_savings_usd AS NUMERIC), 2) AS estimated_cost_savings_usd
FROM
  `driiiportfolio.consumer_ai_analytics.raw_ai_interaction_logs`;
