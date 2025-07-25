# Human Personality Analysis Dashboard

This repository contains a Python-based interactive dashboard built using Dash, Plotly, and Pandas. It's designed to visualize and explore relationships within human personality data, specifically focusing on Introvert and Extrovert types. The project also includes a Jupyter Notebook for initial data preprocessing and analysis.

## Repository Structure

```
.
├── dashboard_app.py              # The main Dash application script
├── data_preprocesssing_and_analysis.ipynb # Jupyter Notebook for data analysis and preprocessing
├── dataset/                      # Directory for data files
│   └── processed_data.csv        # Processed dataset used by the dashboard (expected)
├── requirements.txt              # List of Python dependencies
└── README.md                     # This README file
```

## Features

* **Interactive Scatter Plot:** Explore the relationship between any two selected personality traits. The plot can be color-encoded by personality type (Introvert/Extrovert) to easily distinguish patterns.

* **Interactive Box Plot:** Visualize the distribution of a chosen trait across different personality types, providing insights into their central tendency and spread.

* **Dynamic Axis Selection:** User-friendly dropdown menus allow for on-the-fly selection of X and Y axes for the scatter plot, and the Y-axis for the box plot.

* **Data Analysis Notebook:** The `data_preprocesssing_and_analysis.ipynb` notebook provides a detailed walkthrough of the data loading, cleaning, exploratory data analysis (EDA), and feature engineering steps.

## Setup and Installation

Follow these steps to set up the project and run the dashboard locally.

### 1. Clone the Repository

First, clone this GitHub repository to your local machine:

```bash
git clone [https://github.com/T-emi-dayo/Personality-Analysis-Dashboard.git](https://github.com/T-emi-dayo/Personality-Analysis-Dashboard.git)
cd Personality-Analysis-Dashboard
```

### 2. Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

**Using `venv` (Python's built-in virtual environment):**

```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

**Using `conda` (if you have Anaconda/Miniconda installed):**

```bash
conda create --name personality_dash_env python=3.9
conda activate personality_dash_env
```

### 3. Install Dependencies

With your virtual environment activated, install all required Python packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Data Preparation

The `dashboard_app.py` expects a processed dataset named `processed_data.csv` located in a `dataset/` subfolder.

You can generate this file by running the cells in the `data_preprocesssing_and_analysis.ipynb` Jupyter Notebook. This notebook performs the necessary data loading, cleaning, and preprocessing steps, and saves the final `processed_data.csv` file.

If the `processed_data.csv` file is not found, the dashboard application includes dummy data to allow it to run for demonstration purposes, but it's recommended to generate the actual data using the notebook for full functionality.

### 5. Run the Dashboard Application

Once your environment is active and the data is prepared, run the Dash application:

```bash
python dashboard_app.py
```

After running, open your web browser and navigate to the URL displayed in your terminal (typically `http://127.0.0.1:8050/`).

## Data Preprocessing and Analysis

The `data_preprocesssing_and_analysis.ipynb` notebook covers:

* Importing necessary libraries (Pandas, NumPy, Matplotlib, Seaborn, Plotly).

* Loading the raw dataset.

* Performing exploratory data analysis (EDA) to understand data distributions, missing values, and initial insights.

* Handling categorical and numerical features.

* Generating a correlation matrix to identify relationships between features.

* Saving the cleaned and processed data to `dataset/processed_data.csv`.

## Future Enhancements

* **More Visualization Types:** Integrate additional Plotly chart types (e.g., histograms, violin plots) to offer diverse data perspectives.

* **Advanced Filtering:** Implement more granular filtering options, such as range sliders for numerical features.

* **Improved Responsiveness:** Enhance the dashboard's layout to be fully responsive across various screen sizes (mobile, tablet, desktop).

* **User Authentication:** Add basic user authentication if the dashboard were to be deployed for private use.

* **Database Integration:** Connect the dashboard to a database for dynamic data loading and updates.
