
import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="Goba Capital Simulator", layout="wide")

# Title
st.title("💼 Goba Capital Simulator")

# Input data
st.subheader("Input Parameters")
loan_amount = st.number_input("Financing amount (USD)", min_value=0.0, value=1000000.0, step=10000.0)
annual_rate = st.number_input("Annual effective interest rate (%)", min_value=0.0, value=18.0, step=0.1)
annual_sales = st.number_input("Projected annual sales (USD)", min_value=0.0, value=70000000.0, step=1000000.0)
days_receivables = st.number_input("Average accounts receivable days", min_value=1, value=60, step=1)

# Calculations
daily_sales = annual_sales / 360
avg_receivables = daily_sales * days_receivables
quarterly_rate = (1 + annual_rate / 100) ** (1 / 4) - 1
net_cash_impact = loan_amount - (loan_amount * quarterly_rate)
estimated_growth = (loan_amount / avg_receivables) * annual_sales * 0.1  # example logic

# Show quarterly projections
st.subheader("📈 Quarterly Projections")

try:
    df = pd.DataFrame({
        "Metric": [
            "Average accounts receivable",
            "Quarterly financing cost",
            "Net cash flow impact",
            "Estimated revenue growth"
        ],
        "Value (USD)": [
            round(avg_receivables),
            round(loan_amount * quarterly_rate),
            round(net_cash_impact),
            round(estimated_growth)
        ]
    })

    st.dataframe(df)

    # Display calculation explanation
    st.subheader("📊 Calculation Summary")
    with st.expander("Click to see how the results were calculated"):
        st.markdown(f"""
        - **Daily Sales** = Annual Sales / 360 = {annual_sales:,.2f} / 360 = {daily_sales:,.2f}
        - **Average Receivables** = Daily Sales × Receivable Days = {daily_sales:,.2f} × {days_receivables} = {avg_receivables:,.2f}
        - **Quarterly Rate** = (1 + Annual Rate)^(1/4) - 1 = {(1 + annual_rate / 100):.4f}^(1/4) - 1 = {quarterly_rate:.4%}
        - **Quarterly Financing Cost** = Loan × Quarterly Rate = {loan_amount:,.2f} × {quarterly_rate:.4%} = {loan_amount * quarterly_rate:,.2f}
        - **Net Cash Flow Impact** = Loan - Cost = {loan_amount:,.2f} - {loan_amount * quarterly_rate:,.2f} = {net_cash_impact:,.2f}
        - **Estimated Revenue Growth** ≈ 10% of leverage on receivables = {(loan_amount / avg_receivables):.2f} × {annual_sales:,.2f} × 10% = {estimated_growth:,.2f}
        """)

except Exception as e:
    st.error("There was an error generating the projections.")
    st.exception(e)
