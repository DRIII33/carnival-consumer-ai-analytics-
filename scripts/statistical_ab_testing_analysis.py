# File: scripts/statistical_ab_testing_analysis.py
# Description: Performs two-sample Z-test for proportions on A/B prompt experiment data.

import pandas as pd
import numpy as np
from scipy import stats

def run_ab_test():
    df_ab = pd.read_csv('data/raw_prompt_ab_test_results.csv')

    control = df_ab[df_ab['prompt_variant'] == 'Control_v1.2']['task_completed_successfully']
    variant = df_ab[df_ab['prompt_variant'] == 'Variant_v2.0_PromptRefined']['task_completed_successfully']

    n_control, n_variant = len(control), len(variant)
    p_control, p_variant = control.mean(), variant.mean()

    pooled_p = (control.sum() + variant.sum()) / (n_control + n_variant)
    se = np.sqrt(pooled_p * (1 - pooled_p) * ((1 / n_control) + (1 / n_variant)))
    z_stat = (p_variant - p_control) / se
    p_value = 1 - stats.norm.cdf(z_stat)

    print("=== A/B PROMPT EVALUATION RESULTS ===")
    print(f"Control (v1.2) Success Rate: {p_control * 100:.2f}% (n={n_control})")
    print(f"Variant (v2.0) Success Rate: {p_variant * 100:.2f}% (n={n_variant})")
    print(f"Absolute Lift: {(p_variant - p_control) * 100:.2f}%")
    print(f"Z-Statistic: {z_stat:.4f}")
    print(f"P-Value: {p_value:.6f}")

    if p_value < 0.05:
        print("\nVERDICT: Statistically Significant Improvement! Promote Variant v2.0 to Production.")
    else:
        print("\nVERDICT: No Statistically Significant Difference. Retain Control.")

if __name__ == '__main__':
    run_ab_test()
