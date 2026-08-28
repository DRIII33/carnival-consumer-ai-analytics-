-- File: sql/02_containment_and_intent_analytics.sql
-- Description: Aggregates containment, escalation rates, and cost savings by intent and channel.

CREATE OR REPLACE VIEW `driiiportfolio.consumer_ai_analytics.vw_intent_performance_summary` AS
SELECT
  intent_category,
  channel,
  COUNT(DISTINCT session_id) AS total_sessions,
  SUM(is_contained) AS contained_sessions,
  SUM(is_escalated) AS escalated_sessions,
  ROUND(SAFE_DIVIDE(SUM(is_contained), COUNT(DISTINCT session_id)) * 100, 2) AS containment_rate_pct,
  ROUND(SAFE_DIVIDE(SUM(is_escalated), COUNT(DISTINCT session_id)) * 100, 2) AS escalation_rate_pct,
  ROUND(AVG(turn_count), 1) AS avg_turns_per_session,
  ROUND(AVG(sentiment_score), 2) AS avg_sentiment_score,
  SUM(estimated_cost_savings_usd) AS total_cost_savings_usd
FROM
  `driiiportfolio.consumer_ai_analytics.vw_stg_ai_logs`
GROUP BY
  intent_category,
  channel;
