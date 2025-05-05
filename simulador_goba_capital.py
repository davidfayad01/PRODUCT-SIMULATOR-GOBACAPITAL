
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Goba Capital Simulator", layout="centered")

st.title("📊 Goba Capital Simulator")

# Selección del producto financiero
product = st.selectbox("Select Financial Product", [
    "Factoring",
    "Finance to Suppliers",
    "Asset-Based Lending (ABL)",
    "Loan",
    "Inventory Financing"
])

# Inputs generales
financing_amount = st.number_input("Financing Amount (USD)", min_value=0.0, value=1000000.0, step=10000.0)
annual_interest_rate = st.number_input("Effective Annual Interest Rate (%)", min_value=0.0, value=18.0, step=0.5) / 100
projected_sales = st.number_input("Projected Annual Sales (USD)", min_value=0.0, value=70000000.0, step=1000000.0)
margin = st.number_input("Operating Margin (%)", min_value=0.0, value=12.0, step=0.5) / 100
receivable_days_before = st.number_input("Average Accounts Receivable Days (Before)", min_value=0, value=60)
receivable_days_after = st.number_input("Average Accounts Receivable Days (After)", min_value=0, value=45)

# Cálculos financieros
quarterly_sales = projected_sales / 4
quarterly_margin_profit = quarterly_sales * margin
annual_margin_profit = projected_sales * margin

# Impacto del producto financiero en la caja
cash_flow_gain = 0

if product == "Factoring":
    delta_days = receivable_days_before - receivable_days_after
    daily_sales = projected_sales / 360
    cash_flow_gain = daily_sales * delta_days
elif product == "Finance to Suppliers":
    cash_flow_gain = financing_amount  # financiamiento directo para pagar proveedores
elif product == "Asset-Based Lending (ABL)":
    cash_flow_gain = financing_amount * 0.9  # promedio conservador por colateral
elif product == "Loan":
    cash_flow_gain = financing_amount
elif product == "Inventory Financing":
    cash_flow_gain = financing_amount * 0.95

# Costos financieros
annual_financial_cost = financing_amount * annual_interest_rate
quarterly_financial_cost = annual_financial_cost / 4

# ROI
benefit = cash_flow_gain + annual_margin_profit  # simplificado
roi = (benefit - annual_financial_cost) / financing_amount * 100 if financing_amount else 0

# Mostrar resultados
st.header("📈 Quarterly Financial Impact")
quarterly_df = pd.DataFrame({
    "Q1": [quarterly_sales, quarterly_margin_profit, quarterly_financial_cost],
    "Q2": [quarterly_sales, quarterly_margin_profit, quarterly_financial_cost],
    "Q3": [quarterly_sales, quarterly_margin_profit, quarterly_financial_cost],
    "Q4": [quarterly_sales, quarterly_margin_profit, quarterly_financial_cost],
}, index=["Projected Sales", "Margin Profit", "Financial Cost"])
st.dataframe(quarterly_df.style.format("${:,.0f}"))

st.header("📆 Annual Summary")
st.write(f"💰 **Annual Operating Profit:** ${annual_margin_profit:,.0f}")
st.write(f"📈 **Estimated Cash Flow Gain:** ${cash_flow_gain:,.0f}")
st.write(f"💸 **Annual Financial Cost:** ${annual_financial_cost:,.0f}")
st.write(f"📊 **Estimated ROI:** {roi:.2f}%")
