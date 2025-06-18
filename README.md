# ShadowPersona: Algorithmic Psychology Unveiled

### Project Overview

-----

**ShadowPersona** simulates how social media platforms build **psychological profiles from user engagement data**. This project demonstrates a complete data pipeline, from synthetic data generation and advanced feature engineering to robust orchestration and interactive visualization. It aims to reveal algorithmic influence mechanisms and foster digital awareness.

-----

## Project Demo

-----

Witness the ShadowPersona pipeline and dashboard in action.

### Data Pipeline Execution

Watch the Prefect pipeline automate data generation, transformation, and saving.

*(Replace `path/to/your/pipeline_execution_gif.gif` with a GIF showing your Prefect pipeline running successfully, e.g., from the Prefect UI or console output.)*

### Streamlit Dashboard Walkthrough

Experience the interactive dashboard, exploring user profiles and aggregated insights.

*(Replace `path/to/your/dashboard_interaction_gif.gif` with a GIF demonstrating the Streamlit dashboard's interactivity and key features.)*

-----

## Key Features & Technical Stack

-----

| Feature / Component         | Core Technologies   | Description                                                                 |
| :-------------------------- | :------------------ | :-------------------------------------------------------------------------- |
| **Synthetic Data Generation** | `Faker`, `NumPy`    | Creates realistic user engagement data for profiling simulation.            |
| **Data Processing (EDA & FE)** | `Pandas`            | Cleans, transforms, and engineers features (e.g., rage clicks, doomscroll). |
| **Pipeline Orchestration** | `Prefect`           | Automates and monitors the end-to-end data workflow (MLOps-ready).          |
| **Interactive Dashboard** | `Streamlit`, `Plotly` | Builds dynamic web interface for data visualization and profile exploration.|
| **Modular Design** | Python Best Practices | Ensures maintainable, scalable, and testable codebase.                      |

-----

## Setup and Local Execution

-----

### Prerequisites

  * Python 3.8+
  * `pip` (Python package installer)
  * `git`

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/morte-vi/ShadowPersona-Data-Engineering-Pipeline.git
    cd ShadowPersona-Data-Engineering-Pipeline
    ```

    

2.  **Create and activate virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Running the Project

1.  **Execute the Data Pipeline:**

    ```bash
    python src/data_pipeline.py
    ```

    *(Generates and processes data, saving to `data/shadowpersona_processed_data.csv`)*

2.  **Launch the Streamlit Dashboard:**

    ```bash
    streamlit run src/streamlit_dashboard.py
    ```

    *(Opens dashboard in your browser, typically `http://localhost:8501`)*

-----

## Project Visuals & Reports

-----

This section provides access to detailed analyses, reports, and key visual outputs.

### Streamlit Dashboard Screenshots

See key views of the interactive dashboard:

#### Overall Behavioral Metrics

*(Replace `Assets/streamlit_dash.png` with a screenshot showing aggregate metrics)*

#### Simulated Psychological Trait Distribution

*(Replace `reports/trait_distribution_chart.png` with a screenshot of the trait distribution chart)*

#### Individual User Profile

*(Replace `reports/individual_profile_detail.png` with a screenshot of a detailed individual user profile)*

-----

### EDA & Analysis Reports

Access deeper analytical insights into the generated data.

  * **Exploratory Data Analysis (EDA) Report:**
    **[Link to your EDA Notebook/Report, e.g., `reports/eda_report.html` or a public Jupyter Notebook viewer link]**
    *(Replace with your actual EDA report or link.)*
    *(Optional: Add a small screenshot or GIF of your EDA notebook/report)*

-----

##  Contributing & License

-----

Contributions are welcome\! Feel free to open issues or submit pull requests.

This project is licensed under the [MIT License](https://www.google.com/search?q=LICENSE).


-----
