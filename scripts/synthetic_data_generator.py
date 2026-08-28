# File: scripts/synthetic_data_generator.py
# Description: Generates synthetic interaction logs and A/B testing datasets for SeaSmart AI.

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_synthetic_data():
    np.random.seed(42)
    n_records = 10000

    # Timestamps over 60 days starting June 1, 2026
    start_date = datetime(2026, 6, 1)
    timestamps = [start_date + timedelta(minutes=int(x)) for x in np.random.randint(0, 86400, n_records)]

    intent_categories = [
        'Excursion_Booking', 
        'WiFi_Troubleshooting', 
        'Dining_Reservation', 
        'Folio_Billing_Query', 
        'Baggage_Status'
    ]
    intents = np.random.choice(intent_categories, size=n_records, p=[0.30, 0.25, 0.20, 0.15, 0.10])
    channels = np.random.choice(['Mobile_App_Hub', 'Web_Portal', 'In_Cabin_TV'], size=n_records, p=[0.65, 0.25, 0.10])

    # Operational Metrics
    sentiment_scores = np.random.uniform(-1.0, 1.0, size=n_records).round(2)
    turn_counts = np.random.randint(1, 12, size=n_records)
    containment_flags = np.where((turn_counts < 8) & (sentiment_scores > -0.3), 1, 0)
    escalated_to_human = np.where(containment_flags == 0, 1, 0)

    # Cost Modeling
    cost_per_human_call = 8.50  # USD
    cost_per_ai_interaction = 0.12  # USD
    estimated_savings = np.where(containment_flags == 1, cost_per_human_call - cost_per_ai_interaction, 0.0)

    df_logs = pd.DataFrame({
        'session_id': [f"SESS-{100000 + i}" for i in range(n_records)],
        'guest_id': [f"GST-{np.random.randint(10000, 99999)}" for _ in range(n_records)],
        'interaction_timestamp': timestamps,
        'channel': channels,
        'intent_category': intents,
        'turn_count': turn_counts,
        'sentiment_score': sentiment_scores,
        'is_contained': containment_flags,
        'is_escalated': escalated_to_human,
        'estimated_cost_savings_usd': estimated_savings
    })

    df_logs.to_csv('data/raw_ai_interaction_logs.csv', index=False)
    print(f"Generated data/raw_ai_interaction_logs.csv: {len(df_logs):,} rows.")

    # A/B Prompt Testing Dataset
    n_ab = 2000
    variants = np.random.choice(['Control_v1.2', 'Variant_v2.0_PromptRefined'], size=n_ab, p=[0.5, 0.5])
    success_prob = np.where(variants == 'Variant_v2.0_PromptRefined', 0.84, 0.76)
    task_success = np.random.binomial(1, success_prob)

    df_ab = pd.DataFrame({
        'experiment_id': [f"EXP-{5000 + i}" for i in range(n_ab)],
        'prompt_variant': variants,
        'intent_category': np.random.choice(intent_categories, size=n_ab),
        'task_completed_successfully': task_success,
        'response_latency_seconds': np.random.normal(1.2, 0.3, size=n_ab).round(2)
    })

    df_ab.to_csv('data/raw_prompt_ab_test_results.csv', index=False)
    print(f"Generated data/raw_prompt_ab_test_results.csv: {len(df_ab):,} rows.")

if __name__ == '__main__':
    generate_synthetic_data()
