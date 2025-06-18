# eda_analysis.py (or in a Jupyter Notebook)

import pandas as pd
import numpy as np
import sweetviz as sv # Optional, for quick auto-EDA
# import dtale # Optional, for interactive EDA (might be a bit heavier than sweetviz)

def perform_eda_and_feature_engineering(filepath='data/shadowpersona_user_engagement.csv'):
    """
    Loads data, performs basic EDA, and light feature engineering.
    """
    try:
        df = pd.read_csv(filepath)
        print("Data loaded successfully.")
    except FileNotFoundError:
        print(f"Error: Data file not found at {filepath}. Please run data_generator.py first.")
        return None

    print("\n--- Initial Data Info ---")
    df.info()
    print("\n--- First 5 Rows ---")
    print(df.head())
    print("\n--- Descriptive Statistics ---")
    print(df.describe(include='all'))

    # --- Light Feature Engineering ---
    # Example: Create a 'total_negative_engagement_score'
    df['total_negative_engagement_score'] = df['rage_clicks'] * 0.5 + df['doomscroll_length'] * 0.7

    # Example: Binary feature for "active_notif_responder"
    df['active_notif_responder'] = (~df['notif_response_time'].isna()).astype(int)

    # Example: Simple classification of feed bias
    df['feed_bias_category'] = pd.cut(df['feed_bias_score'], bins=[0, 0.3, 0.7, 1.0],
                                      labels=['left_leaning', 'neutral', 'right_leaning'], include_lowest=True)

    print("\n--- Data after Feature Engineering ---")
    print(df[['rage_clicks', 'doomscroll_length', 'total_negative_engagement_score',
              'notif_response_time', 'active_notif_responder', 'feed_bias_score', 'feed_bias_category']].head())
    print(df.info())

    # --- Optional: Automated EDA (Sweetviz) ---
    # This might take a few seconds but gives a great report.
    # If you have memory issues, comment this out.
    try:
        print("\n--- Generating Sweetviz EDA Report (can be memory intensive for large datasets) ---")
        advert_report = sv.analyze(df)
        advert_report.show_html('reports/eda_report.html') # Default will open in your web browser
        print("Sweetviz report generated: reports/eda_report.html")
    except Exception as e:
        print(f"Could not generate Sweetviz report: {e}. You might be low on memory or Sweetviz might need specific dependencies.")


    return df

if __name__ == "__main__":
    # Ensure 'reports' directory exists
    import os
    if not os.path.exists('reports'):
        os.makedirs('reports')

    processed_df = perform_eda_and_feature_engineering()
    if processed_df is not None:
        print(f"\nProcessed data head:\n{processed_df.head()}")
        # You could save this processed_df if you want
        # processed_df.to_csv('data/processed_user_engagement.csv', index=False)