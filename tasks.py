# tasks.py

import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime
import os

# Import Prefect for tasks
from prefect import task

# --- Data Generation Task ---
@task(name="Generate Synthetic Data")
def generate_data(num_records: int = 5000) -> pd.DataFrame:
    """
    Generates a synthetic dataset for user engagement and psychological profiling.
    Mimics the schema: shadowpersona_user_engagement.csv
    Returns:
        pd.DataFrame: A DataFrame containing the simulated user engagement data.
    """
    print(f"Generating {num_records} synthetic records...")
    fake = Faker()
    data = []

    # Define possible ad click emotions and categories
    ad_emotions = ['anger', 'curiosity', 'joy', 'sadness', 'surprise', 'neutral']
    ad_categories = ['finance', 'travel', 'fashion', 'tech', 'food', 'gaming', 'news']

    # Define possible psychological traits (for 'predicted_trait_label' - this would normally be an ML output)
    psych_traits = ['anxious', 'impulsive', 'curious', 'skeptical', 'compliant', 'distracted']

    for i in range(num_records):
        user_id = f"user_{i:05d}"
        session_time = np.random.randint(5, 120) # 5 to 120 minutes
        rage_clicks = np.random.randint(0, 15) if np.random.rand() < 0.3 else 0 # 30% chance of rage clicks
        doomscroll_length = np.random.uniform(0, 60) if np.random.rand() < 0.5 else 0 # 50% chance of doomscrolling
        ad_click_emotion = random.choice(ad_emotions)
        feed_bias_score = np.random.uniform(0, 1) # 0 to 1
        
        # Simulate notification time within a day
        base_time = datetime(2023, 1, 1, np.random.randint(8, 23), np.random.randint(0, 59))
        notification_time_str = base_time.strftime("%H:%M:%S")

        notif_response_time = np.random.uniform(1, 60) if np.random.rand() < 0.7 else np.nan # 70% response, otherwise NaN
        keyword_sentiment_score = np.random.uniform(-1, 1) # -1 (negative) to 1 (positive)
        ad_category_clicked = random.choice(ad_categories)

        # Simulate predicted_trait_label based on some simple rules for demonstration
        # In a real scenario, this would come from your ML model.
        # Here, we're just creating plausible "ground truth" for the simulated data.
        if rage_clicks > 5 or doomscroll_length > 30:
            predicted_trait_label = random.choice(['anxious', 'impulsive'])
        elif keyword_sentiment_score < -0.5:
            predicted_trait_label = 'skeptical'
        elif ad_click_emotion == 'curiosity':
            predicted_trait_label = 'curious'
        else:
            predicted_trait_label = random.choice(psych_traits) # pick from all if no specific rule matched

        data.append({
            'user_id': user_id,
            'session_time': session_time,
            'rage_clicks': rage_clicks,
            'doomscroll_length': doomscroll_length,
            'ad_click_emotion': ad_click_emotion,
            'feed_bias_score': feed_bias_score,
            'notification_time': notification_time_str,
            'notif_response_time': notif_response_time,
            'keyword_sentiment_score': keyword_sentiment_score,
            'ad_category_clicked': ad_category_clicked,
            'predicted_trait_label': predicted_trait_label
        })

    df = pd.DataFrame(data)
    print(f"Generated {len(df)} records.")
    return df

# --- Feature Engineering Task ---
@task(name="Perform Feature Engineering")
def feature_engineer_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs light feature engineering on the input DataFrame.
    Calculates derived features such as total_negative_engagement_score,
    active_notif_responder, and feed_bias_category.
    Args:
        df (pd.DataFrame): The input DataFrame.
    Returns:
        pd.DataFrame: The DataFrame with new features added.
    """
    print("Performing feature engineering...")
    df['total_negative_engagement_score'] = df['rage_clicks'] * 0.5 + df['doomscroll_length'] * 0.7
    df['active_notif_responder'] = (~df['notif_response_time'].isna()).astype(int)
    
    # Ensure feed_bias_score is numeric before cutting
    df['feed_bias_score'] = pd.to_numeric(df['feed_bias_score'], errors='coerce')
    df['feed_bias_category'] = pd.cut(df['feed_bias_score'], bins=[0, 0.3, 0.7, 1.0],
                                      labels=['left_leaning', 'neutral', 'right_leaning'], include_lowest=True, right=True)
    
    print("Feature engineering complete.")
    print("New features added:", ['total_negative_engagement_score', 'active_notif_responder', 'feed_bias_category'])
    return df

# --- Data Saving Task ---
@task(name="Save Processed Data")
def save_data(df: pd.DataFrame, output_path: str):
    """
    Saves the DataFrame to a specified CSV path.
    Args:
        df (pd.DataFrame): The DataFrame to save.
        output_path (str): The full path including filename to save the CSV.
    """
    print(f"Saving data to {output_path}...")
    # Ensure the directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Data saved successfully to {output_path}.")