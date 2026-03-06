# Coffee Roasters Sales Analytics Dashboard

## Project Overview

This project analyzes retail sales data from a coffee roastery in order to identify top-performing products, sales distribution patterns, and key revenue drivers.

The analysis combines Python data processing with visual analytics and an interactive dashboard. The goal is to demonstrate practical data analytics skills including data cleaning, exploratory analysis, visualization, and dashboard development.

---

## Dataset

The dataset contains transactional retail sales information including:

* Coffee product names
* Sales quantities
* Revenue values
* Product performance indicators

The dataset was cleaned and prepared before analysis to ensure consistency and usability.

---

## Tools & Technologies

* Python
* Pandas
* Matplotlib
* Jupyter Notebook
* Streamlit
* GitHub

---

## Key Analysis

The analysis focuses on identifying high-value products and understanding how revenue is distributed across the product portfolio.

Main analytical components include:

* Product sales ranking
* Top 10 product performance
* Pareto analysis (80/20 principle)
* Sales distribution visualization

The Pareto analysis highlights which small group of products generates the majority of total revenue.

---

## Interactive Dashboard

An interactive dashboard was created using Streamlit to present the analysis results.

Dashboard features include:

* Top product sales overview
* Pareto chart visualization
* Product performance comparison
* Clear visual insights into revenue concentration

---
## Dashboard Preview

### Streamlit Dashboard

![Dashboard](images/dashboard.png)

### Pareto Analysis

![Pareto Chart](images/pareto_chart.png)

### Sales Distribution

![Sales Chart](images/sales_chart.png)
## Key Insights

Key insights from the analysis include:

* A small number of products generate the majority of total sales.
* The top-selling items dominate overall revenue contribution.
* Product-level analysis helps identify priority items for inventory and marketing focus.

These findings support data-driven decision-making in retail operations.

---

## Repository Structure

```
coffee-roasters-sales-analytics

data/
    cleaned_coffee_dataset.csv

notebooks/
    coffee_sales_analysis.ipynb

app/
    streamlit_dashboard.py

images/
    charts_and_dashboard_screenshots

README.md
requirements.txt
report.pdf
```

---

## How to Run the Project

1. Clone the repository

```
git clone https://github.com/yourusername/coffee-roasters-sales-analytics.git
```

2. Install required libraries

```
pip install -r requirements.txt
```

3. Run the Streamlit dashboard

```
streamlit run streamlit_dashboard.py
```

---

## Project Purpose

This project was created as part of a data analytics portfolio to demonstrate practical skills in:

* Data analysis
* Data visualization
* Dashboard development
* Python analytics workflows

The project illustrates how sales data can be transformed into actionable insights using modern analytics tools.

