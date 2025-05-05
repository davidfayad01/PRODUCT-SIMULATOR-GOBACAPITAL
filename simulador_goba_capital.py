
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Goba Capital Simulator", layout="centered")

st.title("📊 Goba Capital Simulator")

# Inputs
loan_amount = st.number_input("Financing Amount (USD)", min_value=0.0, value=1000000.0, step=10000.0)
annual_rate = st.number_input("Effective Annual Interest Rate (%)", min_value=0.0, value=18.0, step=0.1)
annual_sales = st.number_input("Projected Annual Sales (USD)", min_value=0.0, value=70000000.0, step=1000000.0)
avg_receivables_days = st.number_input("Average Accounts Receivable Days", min_value=1, value=60, step=1)

# Avoid division by zero or missing inputs
if annual_sales > 0 and annual_rate > 0 and loan_amount > 0:
    interest_cost = loan_amount * (annual_rate / 100)
    quarterly_sales = annual_sales / 4
    interest_quarterly = interest_cost / 4

    df = pd.DataFrame({
        "Quarter": ["Q1", "Q2", "Q3", "Q4"],
        "Projected Sales (USD)": [quarterly_sales] * 4,
        "Interest Cost (USD)": [interest_quarterly] * 4,
        "Net Cash Flow (USD)": [quarterly_sales - interest_quarterly] * 4
    })

    st.subheader("📈 Quarterly Projections")
    st.dataframe(df.style.format("{:,.0f}"))

    st.subheader("📅 Annual Summary")
    st.write(f"**Total Projected Sales:** USD {annual_sales:,.0f}")
    st.write(f"**Total Interest Cost:** USD {interest_cost:,.0f}")
    st.write(f"**Annual Net Cash Flow:** USD {annual_sales - interest_cost:,.0f}")
else:
    st.warning("Please fill in all input fields with values greater than zero to see projections.")
