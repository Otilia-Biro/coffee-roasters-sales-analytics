import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(
    page_title="Afficionado Coffee Roasters Dashboard",
    layout="wide"
)

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_afficionado_dataset.csv")

try:
    df = load_data()
    st.success("Dataset loaded successfully!")
except FileNotFoundError:
    st.error("ERROR: cleaned_afficionado_dataset.csv not found in the project folder.")
    st.stop()

# Title
st.title("☕ Coffee Retail Analytics Dashboard")
st.markdown("Product Revenue & Menu Performance Analysis")

# Sidebar Filters
st.sidebar.header("Filter Options")

selected_category = st.sidebar.multiselect(
    "Select Product Category",
    options=sorted(df["product_category"].unique()),
    default=sorted(df["product_category"].unique())
)

selected_type = st.sidebar.multiselect(
    "Select Product Type",
    options=sorted(df["product_type"].unique()),
    default=sorted(df["product_type"].unique())
)

# Apply Filters
filtered_df = df[
    (df["product_category"].isin(selected_category)) &
    (df["product_type"].isin(selected_type))
]

# KPIs
st.subheader("Key Performance Indicators")

total_revenue = filtered_df["revenue"].sum()
total_units = filtered_df["transaction_qty"].sum()
avg_revenue = filtered_df["revenue"].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Units Sold", f"{total_units:,}")
col3.metric("Average Revenue per Transaction", f"${avg_revenue:,.2f}")

# Top 10 Products by Revenue
st.subheader("Top 10 Products by Revenue")

top_products = (
    filtered_df.groupby("product_detail")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.barplot(data=top_products, x="revenue", y="product_detail", ax=ax1)
ax1.set_title("Top 10 Revenue-Generating Products")
ax1.set_xlabel("Total Revenue")
ax1.set_ylabel("Product Detail")
st.pyplot(fig1)

# Bottom 10 Products
st.subheader("Bottom 10 Products by Revenue")

bottom_products = (
    filtered_df.groupby("product_detail")["revenue"]
    .sum()
    .sort_values(ascending=True)
    .head(10)
    .reset_index()
)

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(data=bottom_products, x="revenue", y="product_detail", ax=ax2)
ax2.set_title("Lowest Revenue-Generating Products")
ax2.set_xlabel("Total Revenue")
ax2.set_ylabel("Product Detail")
st.pyplot(fig2)

# Revenue by Category
st.subheader("Revenue Distribution by Category")

category_revenue = (
    filtered_df.groupby("product_category")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.barplot(data=category_revenue, x="revenue", y="product_category", ax=ax3)
ax3.set_title("Revenue by Product Category")
ax3.set_xlabel("Total Revenue")
ax3.set_ylabel("Category")
st.pyplot(fig3)

st.subheader("Revenue vs Units Sold (Product Performance)")

scatter_data = (
    filtered_df.groupby("product_detail")
    .agg({
        "revenue": "sum",
        "transaction_qty": "sum"
    })
    .reset_index()
)

fig3, ax3 = plt.subplots(figsize=(8,6))

sns.scatterplot(
    data=scatter_data,
    x="transaction_qty",
    y="revenue"
)

ax3.set_title("Revenue vs Units Sold")
ax3.set_xlabel("Total Units Sold")
ax3.set_ylabel("Total Revenue")

st.pyplot(fig3)

# Pareto Analysis
st.subheader("Pareto Analysis (Revenue Concentration)")

pareto_df = (
    filtered_df.groupby("product_detail")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

pareto_df["cumulative_percentage"] = (
    pareto_df["revenue"].cumsum() / pareto_df["revenue"].sum() * 100
)

st.line_chart(pareto_df.set_index("product_detail")["cumulative_percentage"])

# Data Preview
st.subheader("Filtered Dataset Preview")
st.dataframe(filtered_df.head(20))