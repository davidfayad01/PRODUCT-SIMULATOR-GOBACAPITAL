
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Simulador Financiamiento - Goba Capital")

st.title("📊 Simulador de Financiamiento Empresarial")
st.subheader("Impacto de productos como Factoring, ABL y Pago a Proveedores")

# Entradas del usuario
ventas_anuales = st.number_input("Ventas anuales (USD):", min_value=0, value=10000000, step=100000)
dso = st.number_input("Días de cuentas por cobrar (DSO):", min_value=0, value=60)
dio = st.number_input("Días de inventario (DIO):", min_value=0, value=45)
dpo = st.number_input("Días de cuentas por pagar (DPO):", min_value=0, value=30)
margen_operativo = st.slider("Margen operativo (%):", 0, 100, 15)
monto_financiamiento = st.number_input("Monto del financiamiento (USD):", min_value=0, value=2000000, step=50000)
tasa_efectiva_anual = st.number_input("Tasa efectiva anual (%):", min_value=0.0, value=18.0, step=0.1)
producto = st.selectbox("Producto financiero:", ["Factoring", "ABL (Asset Based Lending)", "Pago a Proveedores"])

# Cálculos
ciclo_operativo = dso + dio - dpo
ventas_diarias = ventas_anuales / 360
capital_trabajo_actual = ventas_diarias * ciclo_operativo
capital_trabajo_post_financiamiento = max(capital_trabajo_actual - monto_financiamiento, 0)

# Mejoras
flujo_adicional = capital_trabajo_actual - capital_trabajo_post_financiamiento
crecimiento_ventas = flujo_adicional * 4  # supuestos de apalancamiento comercial
nuevas_ventas_anuales = ventas_anuales + crecimiento_ventas
nueva_utilidad = nuevas_ventas_anuales * (margen_operativo / 100)
costo_financiero = monto_financiamiento * (tasa_efectiva_anual / 100)
roi_financiamiento = ((nueva_utilidad - (ventas_anuales * (margen_operativo / 100))) - costo_financiero) / costo_financiero * 100

# Resultados
st.markdown("---")
st.header("📈 Resultados")

col1, col2 = st.columns(2)
col1.metric("🕒 Ciclo operativo actual (días)", f"{ciclo_operativo} días")
col1.metric("💵 Capital de trabajo liberado", f"USD {flujo_adicional:,.0f}")
col2.metric("📊 Nuevas ventas estimadas", f"USD {nuevas_ventas_anuales:,.0f}")
col2.metric("💡 ROI del financiamiento", f"{roi_financiamiento:.2f}%")

# Tabla comparativa trimestral
df = pd.DataFrame({
    "Trimestre": ["Q1", "Q2", "Q3", "Q4"],
    "Ventas (USD)": [nuevas_ventas_anuales / 4] * 4,
    "Utilidad (USD)": [nueva_utilidad / 4] * 4,
    "Costo Financiero (USD)": [costo_financiero / 4] * 4
})
st.markdown("### 📅 Proyecciones Trimestrales")
st.dataframe(df.style.format("{:.0f}"))

st.markdown("---")
st.caption("Simulador diseñado por Goba Capital. Resultados estimados, no contractuales.")
