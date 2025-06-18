# ShadowPersona: Algorithmic Psychology Unveiled

### Project Overview

-----

**ShadowPersona** simulates how social media platforms build **psychological profiles from user engagement data**. This project demonstrates a complete data pipeline, from synthetic data generation and advanced feature engineering to robust orchestration and interactive visualization. It aims to reveal algorithmic influence mechanisms and foster digital awareness.

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
![streamlit_dash](https://github.com/user-attachments/assets/1f935621-3325-46d2-9b07-c3ac813d98cd)



#### Simulated Psychological Trait Distribution

![streamlit_dash2](https://github.com/user-attachments/assets/24cb9f70-fc9e-4e80-8677-3524b491ff2e)


### EDA & Analysis Reports (Interactive)

Access deeper analytical insights into the generated data.

Overall Report Dashboard 

![Screenshot 2025-06-18 at 9 55 39 PM](https://github.com/user-attachments/assets/b8096c7a-3209-4e0a-abf9-8fe92be13720)

Rage Clicks Report 

![Screenshot 2025-06-18 at 9 57 04 PM](https://github.com/user-attachments/assets/325ca7ec-2f9f-4885-baa5-21791892b702)

DoomScroll Length Report

![Screenshot 2025-06-18 at 9 57 57 PM](https://github.com/user-attachments/assets/576ff42a-5ef4-405f-9f87-6ec2fc2d2c0e)

Notification Response Time Report

![Screenshot 2025-06-18 at 9 58 51 PM](https://github.com/user-attachments/assets/f3e849a9-d82e-4d0c-95db-e44c614e316e)

Ad Category Clicked Report 

![Screenshot 2025-06-18 at 9 59 53 PM](https://github.com/user-attachments/assets/ebe1f696-7160-43ff-b09d-02668afc5440)

-----

##  Contributing & License

-----

Contributions are welcome\! Feel free to open issues or submit pull requests.

This project is licensed under the [MIT License](https://www.google.com/search?q=LICENSE).


-----
