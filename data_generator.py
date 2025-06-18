# data_generator.py

import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

def generate_user_engagement_data(num_records=1000):
    """
    Generates a synthetic dataset for user engagement and psychological profiling.
    Mimics the schema: shadowpersona_user_engagement.csv
    """
    fake = Faker()
    data = []

    # Define possible ad click emotions and categories
    ad_emotions = ['anger', 'curiosity', 'joy', 'sadness', 'surprise', 'neutral']
    ad_categories = ['finance', 'travel', 'fashion', 'tech', 'food', 'gaming', 'news']

    # Define possible psychological traits (for 'predicted_trait_label' - this would normally be an ML output)
    # We'll assign these probabilistically for simulation purposes.
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
            'predicted_trait_label': predicted_trait_label # This is the "ground truth" for simulation
        })

    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    print("Generating synthetic user engagement data...")
    df = generate_user_engagement_data(num_records=5000) # Generate 5000 records
    df.to_csv('data/shadowpersona_user_engagement.csv', index=False)
    print(f"Data generated and saved to data/shadowpersona_user_engagement.csv with {len(df)} records.")
    print(df.head())
    print(df.info())