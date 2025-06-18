# streamlit_dashboard.py

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os # Import os to check for file existence


DATA_PATH = 'data/shadowpersona_processed_data.csv'


st.set_page_config(layout="wide", page_title="ShadowPersona Dashboard")

# --- Data Loading ---
@st.cache_data 
def load_processed_data():
    """
    Loads the processed user engagement data from the specified CSV path.
    Assumes the data has been generated and processed by the Prefect pipeline.
    """
    if not os.path.exists(DATA_PATH):
        st.error(f"Data file not found at {DATA_PATH}. Please run `python data_pipeline.py` first to generate it.")
        return pd.DataFrame()
    
    try:
        df = pd.read_csv(DATA_PATH)
        
        df['session_time'] = df['session_time'].astype(int)
        df['rage_clicks'] = df['rage_clicks'].astype(int)
        df['doomscroll_length'] = df['doomscroll_length'].astype(float)
        df['feed_bias_score'] = df['feed_bias_score'].astype(float)
        
        # Handle NaN for notif_response_time (important if you have it in your data)
        df['notif_response_time'] = df['notif_response_time'].replace([np.inf, -np.inf], np.nan)
        
        print(f"Data loaded successfully from {DATA_PATH} with {len(df)} records.")
        return df
    except Exception as e:
        st.error(f"Error loading or processing data from {DATA_PATH}: {e}")
        return pd.DataFrame()

df = load_processed_data()

# --- Streamlit App Layout ---
# The rest of your app logic now correctly follows the page config
if not df.empty:
    st.title("ShadowPersona: Algorithmic Psychology Unveiled")
    st.markdown("""
    This dashboard simulates the outputs of **ShadowPersona**, a project designed to
    reverse-engineer the psychological profiling mechanisms used by social platforms.
    It visualizes how behavioral data can reveal algorithmic exploitation for retention and manipulation.

    *Data processed via Prefect pipeline.*
    """)

    st.sidebar.header("Dashboard Controls")
    
    # Check if 'user_id' column exists before getting unique values
    if 'user_id' in df.columns and not df['user_id'].empty:
        selected_user = st.sidebar.selectbox("Select User ID (for detailed profile):", df['user_id'].unique())
    else:
        selected_user = None
        st.sidebar.warning("No user IDs found in data for selection.")

    # Check if 'predicted_trait_label' exists
    if 'predicted_trait_label' in df.columns and not df['predicted_trait_label'].empty:
        selected_trait_filter = st.sidebar.multiselect(
            "Filter by Predicted Trait:",
            options=df['predicted_trait_label'].unique(),
            default=df['predicted_trait_label'].unique()
        )
        filtered_df = df[df['predicted_trait_label'].isin(selected_trait_filter)]
    else:
        selected_trait_filter = []
        filtered_df = df.copy()
        st.sidebar.warning("No psychological trait labels found in data for filtering.")


    # --- Overall Engagement Metrics ---
    st.header("Overall Behavioral Metrics")
    col1, col2, col3, col4, col5 = st.columns(5) # Added one more column for new metric
    
    with col1:
        st.metric("Avg Session Time (min)", f"{df['session_time'].mean():.1f}")
    with col2:
        st.metric("Avg Doomscroll Length (min)", f"{df['doomscroll_length'].mean():.1f}")
    with col3:
        st.metric("Avg Rage Clicks", f"{df['rage_clicks'].mean():.1f}")
    with col4:
        # Use the newly engineered 'active_notif_responder'
        st.metric("Notification Response Rate", f"{(df['active_notif_responder'].sum() / len(df) * 100):.1f}%")
    with col5:
        # New metric from engineered feature
        st.metric("Avg Negative Engagement Score", f"{df['total_negative_engagement_score'].mean():.1f}")


    # --- Distribution of Predicted Traits ---
    if 'predicted_trait_label' in filtered_df.columns and not filtered_df['predicted_trait_label'].empty:
        st.header("Distribution of Simulated Psychological Traits")
        trait_counts = filtered_df['predicted_trait_label'].value_counts().reset_index()
        trait_counts.columns = ['Trait', 'Count']
        fig_traits = px.bar(trait_counts, x='Trait', y='Count', color='Trait',
                            title='Simulated Psychological Trait Distribution',
                            labels={'Trait': 'Predicted Trait', 'Count': 'Number of Users'})
        st.plotly_chart(fig_traits, use_container_width=True)
    else:
        st.info("Trait distribution cannot be displayed as 'predicted_trait_label' column is missing or empty in filtered data.")


    # --- Engagement Heatmap (Simulated) ---
    st.header("Engagement Heatmap (Simulated)")
    st.markdown("This heatmap visualizes how different traits might correlate with key engagement patterns.")
    
    # Ensure columns exist before using them for heatmap
    if all(col in filtered_df.columns for col in ['predicted_trait_label', 'session_time', 'doomscroll_length', 'rage_clicks', 'total_negative_engagement_score']):
        heatmap_data = filtered_df.groupby('predicted_trait_label')[['session_time', 'doomscroll_length', 'rage_clicks', 'total_negative_engagement_score']].mean().reset_index()
        fig_heatmap = px.imshow(heatmap_data.set_index('predicted_trait_label'),
                                text_auto=True, color_continuous_scale='Viridis',
                                title='Average Engagement Metrics by Simulated Trait')
        st.plotly_chart(fig_heatmap, use_container_width=True)
    else:
        st.info("Engagement heatmap cannot be displayed due to missing key columns.")


    # --- Ad Emotion Clusters (Simulated) ---
    if all(col in filtered_df.columns for col in ['ad_click_emotion', 'ad_category_clicked']):
        st.header("Ad Emotion & Category Distribution")
        col_ad1, col_ad2 = st.columns(2)
        with col_ad1:
            ad_emotion_counts = filtered_df['ad_click_emotion'].value_counts().reset_index()
            ad_emotion_counts.columns = ['Emotion', 'Count']
            fig_ad_emotion = px.pie(ad_emotion_counts, values='Count', names='Emotion',
                                    title='Distribution of Ad Click Emotions')
            st.plotly_chart(fig_ad_emotion, use_container_width=True)
        with col_ad2:
            ad_category_counts = filtered_df['ad_category_clicked'].value_counts().reset_index()
            ad_category_counts.columns = ['Category', 'Count']
            fig_ad_category = px.bar(ad_category_counts, x='Category', y='Count', color='Category',
                                    title='Distribution of Ad Categories Clicked')
            st.plotly_chart(fig_ad_category, use_container_width=True)
    else:
        st.info("Ad emotion and category distributions cannot be displayed due to missing columns.")


    # --- Individual User Profile (Simulated 'Report') ---
    if selected_user:
        st.header(f"Simulated Psychological Profile for User: `{selected_user}`")
        user_data = df[df['user_id'] == selected_user].iloc[0]

        st.subheader("Behavioral Snapshot:")
        col_u1, col_u2, col_u3 = st.columns(3)
        with col_u1:
            st.write(f"**Predicted Trait:** `{user_data.get('predicted_trait_label', 'N/A').capitalize()}`")
            st.write(f"**Session Time:** `{user_data.get('session_time', 'N/A')} minutes`")
            st.write(f"**Doomscroll Length:** `{user_data.get('doomscroll_length', 'N/A'):.1f} minutes`")
            st.write(f"**Total Negative Engagement Score:** `{user_data.get('total_negative_engagement_score', 'N/A'):.1f}`") # New
        with col_u2:
            st.write(f"**Rage Clicks:** `{user_data.get('rage_clicks', 'N/A')}`")
            st.write(f"**Ad Click Emotion:** `{user_data.get('ad_click_emotion', 'N/A').capitalize()}`")
            st.write(f"**Ad Category Clicked:** `{user_data.get('ad_category_clicked', 'N/A').capitalize()}`")
        with col_u3:
            st.write(f"**Feed Bias Score:** `{user_data.get('feed_bias_score', 'N/A'):.2f}` ({user_data.get('feed_bias_category', 'N/A').capitalize()})") # New
            st.write(f"**Notification Time:** `{user_data.get('notification_time', 'N/A')}`")
            if pd.isna(user_data.get('notif_response_time')):
                st.write(f"**Notification Response:** `No Response`")
            else:
                st.write(f"**Notification Response:** `{user_data.get('notif_response_time', 'N/A'):.1f} seconds`")
            st.write(f"**Active Notif Responder:** `{'Yes' if user_data.get('active_notif_responder') == 1 else 'No'}`") # New

        st.subheader("Simulated Model Explainability (Concept):")
        st.markdown(f"""
        **Why was `{selected_user}` profiled as `{user_data.get('predicted_trait_label', 'N/A').capitalize()}`?**

        *(Note: This is a simulated explanation. In a real project, this would be generated by SHAP/LIME based on a trained ML model's features and their impact.)*

        * **High Negative Engagement:** User exhibited a high **Total Negative Engagement Score** (`{user_data.get('total_negative_engagement_score', 'N/A'):.1f}`), primarily driven by significant **doomscrolling** (`{user_data.get('doomscroll_length', 'N/A'):.1f}` minutes) and notable **rage clicks** (`{user_data.get('rage_clicks', 'N/A')}`). These behaviors are often strong indicators of **{user_data.get('predicted_trait_label', 'N/A')}** patterns.
        * **Content and Ad Interactions:** Their interaction with ads classified as **'{user_data.get('ad_click_emotion', 'N/A')}' emotion** and content consumed with a **'{user_data.get('feed_bias_category', 'N/A')}' feed bias** may also align with patterns observed in users with **{user_data.get('predicted_trait_label', 'N/A')}** tendencies.
        * **Responsiveness:** Their **notification response behavior** (`{'responded' if user_data.get('active_notif_responder') == 1 else 'did not respond'}`) can further contribute to the profiling, suggesting their level of engagement with platform nudges.
        """)

    st.markdown("---")
    st.info("💡 This dashboard demonstrates the visualization capabilities of ShadowPersona. Actual psychological profiling would involve trained machine learning models and more complex explainability techniques.")