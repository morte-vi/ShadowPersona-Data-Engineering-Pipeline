# data_pipeline.py
from prefect import flow
from tasks import generate_data, feature_engineer_data, save_data

@flow(name="ShadowPersona Data Pipeline", log_prints=True)
def shadowpersona_data_pipeline(num_records: int = 5000, output_filename: str = 'shadowpersona_processed_data.csv'):
    """
    Orchestrates the data generation, feature engineering, and saving steps.
    """
    print("Starting ShadowPersona Data Pipeline...")
    
    # 1. Generate Raw Data
    raw_df = generate_data(num_records=num_records)

    # 2. Perform Feature Engineering
    processed_df = feature_engineer_data(df=raw_df)

    # 3. Save Processed Data
    save_data(df=processed_df, output_path=f"data/{output_filename}")
    
    print("ShadowPersona Data Pipeline completed successfully.")

if __name__ == "__main__":
    # To run the pipeline locally:
    shadowpersona_data_pipeline(num_records=10000) # You can adjust num_records