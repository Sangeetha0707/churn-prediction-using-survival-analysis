import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Streamlit App Setup
st.set_page_config(
    page_title="Simple Churn Data Viewer",
    layout="centered"
)
st.title("📄 Simple Churn Data Visualization")
st.markdown("Upload your dataset to see basic tenure and churn rate plots.")
st.markdown("---")

# 2. File Uploader
uploaded_file = st.file_uploader(
    "Upload your Churn Dataset (CSV/XLSX)",
    type=["csv", "xlsx"]
)

if uploaded_file:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Unsupported file type.")
            st.stop()
            
        # column names for checking
        df.columns = [col.lower() for col in df.columns]

        # Check for essential columns (Duration 'tenure' and Event 'churn')
        if 'tenure' not in df.columns or 'churn' not in df.columns:
            st.error("Error: Dataset must contain columns named 'tenure' (for duration) and 'churn' (for status, e.g., Yes/No).")
            st.stop()

    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()
    
    # 4. Display Basic Data & Statistics
    st.success(f"Data Loaded! Total Customers: {len(df)}")
    st.subheader("First 5 Rows of Data")
    st.dataframe(df.head())
    
    # 5. Visualization 1: Tenure Distribution 
    st.header("1. Customer Tenure Distribution")
    st.markdown("This chart shows how long customers have stayed with the company.")
    
    # Simple Matplotlib Histogram
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    ax1.hist(df['tenure'].dropna(), bins=30, color='skyblue', edgecolor='black')
    ax1.set_title("Distribution of Customer Tenure (Months)")
    ax1.set_xlabel("Tenure (Months)")
    ax1.set_ylabel("Number of Customers")
    st.pyplot(fig1)

    # 6. Visualization 2: Churn Status 
    st.header("2. Churn Status Count")
    st.markdown("This chart shows the total number of customers who have churned.")

    # Simple Matplotlib Bar Chart
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    
    # Map churn column (assuming Yes/No)
    churn_counts = df['churn'].astype(str).str.lower().value_counts()
    churn_counts.plot(kind='bar', ax=ax2, color=['lightcoral', 'lightgreen'])
    
    ax2.set_title("Churned vs. Non-Churned Customers")
    ax2.set_xlabel("Churn Status (Yes = Churned, No = Not Churned)")
    ax2.set_ylabel("Number of Customers")
    ax2.tick_params(axis='x', rotation=0)
    st.pyplot(fig2)





