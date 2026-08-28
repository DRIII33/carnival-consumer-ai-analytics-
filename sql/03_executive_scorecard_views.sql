-- File: sql/03_executive_scorecard_views.sql
-- Description: Daily executive scorecard view for Looker Studio consumption.

CREATE OR REPLACE VIEW `driiiportfolio.consumer_ai_analytics.vw_executive_scorecard_kpis` AS
SELECT
  interaction_date,
  intent_category,
  COUNT(DISTINCT session_id) AS total_interactions,
  ROUND(AVG(containment_rate_pct), 2) AS avg_containment_rate_pct,
  SUM(total_cost_savings_usd) AS daily_cost_savings_usd,
  ROUND(AVG(avg_sentiment_score), 2) AS net_sentiment_score
FROM
  `driiiportfolio.consumer_ai_analytics.vw_intent_performance_summary`,
  UNNEST([1])
GROUP BY
  interaction_date,
  intent_category;
