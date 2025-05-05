
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Goba Capital Simulator", layout="centered")

st.title("📊 Goba Capital Simulator")

# Inputs
financing_amount = st.number_input("Financing Amount (USD)", min_value=0.0, step=10000.0, value=1000000.0, format="%.2f")
annual_interest_rate = st.number_input("Effective Annual Interest Rate (%)", min_value=0.0, step=0.1, value=18.0, format="%.2f")
projected_sales = st.number_input("Projected Annual Sales (USD)", min_value=0.0, step=10000.0, value=70000000.0, format="%.2f")
days_receivable = st.number_input("Average Accounts Receivable Days", min_value=0, step=1, value=60)

# Calculations
quarterly_sales = projected_sales / 4
daily_sales = projected_sales / 360
reduction_in_receivables = daily_sales * days_receivable
annual_savings = reduction_in_receivables
quarterly_savings = annual_savings / 4
interest_cost = financing_amount * (annual_interest_rate / 100)
net_benefit = annual_savings - interest_cost

# Create projections table
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Projected Sales (USD)": [quarterly_sales] * 4,
    "Improved Cash Flow (USD)": [quarterly_savings] * 4,
    "Interest Cost (USD)": [interest_cost / 4] * 4,
    "Net Quarterly Benefit (USD)": [quarterly_savings - (interest_cost / 4)] * 4,
}

df = pd.DataFrame(data)

st.subheader("📈 Quarterly Projections")

# Safe formatting
try:
    st.dataframe(df.style.format({
        "Projected Sales (USD)": "${:,.0f}",
        "Improved Cash Flow (USD)": "${:,.0f}",
        "Interest Cost (USD)": "${:,.0f}",
        "Net Quarterly Benefit (USD)": "${:,.0f}"
    }))
except:
    st.dataframe(df)

# Annual summary
st.subheader("📘 Annual Summary")
st.markdown(f"**Total Improved Cash Flow:** ${annual_savings:,.0f}")
st.markdown(f"**Total Interest Cost:** ${interest_cost:,.0f}")
st.markdown(f"**Net Annual Benefit:** ${net_benefit:,.0f}")
