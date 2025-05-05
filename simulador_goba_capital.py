
import streamlit as st
import pandas as pd

st.title("Simulador Financiero - Goba Capital")

# Inputs
monto_financiamiento = st.number_input("Monto del financiamiento (USD)", min_value=1000000, step=100000)
tasa_anual = st.number_input("Tasa de interés efectiva anual (%)", min_value=0.0, step=0.1) / 100
ventas_anuales = st.number_input("Ventas proyectadas anuales (USD)", min_value=0.0, step=10000.0)
dias_cartera = st.number_input("Días promedio de cuentas por cobrar", min_value=0, value=60)

# Cálculos base
costo_financiamiento = monto_financiamiento * tasa_anual
mejora_caja = ventas_anuales * (dias_cartera / 360)
crecimiento_estimado = mejora_caja * 0.15

# Proyecciones trimestrales
proyecciones = {
    "Trimestre": ["Q1", "Q2", "Q3", "Q4"],
    "Financiamiento Recibido (USD)": [monto_financiamiento / 4] * 4,
    "Costo Financiamiento (USD)": [costo_financiamiento / 4] * 4,
    "Mejora Flujo Caja (USD)": [mejora_caja / 4] * 4,
    "Crecimiento Estimado (USD)": [crecimiento_estimado / 4] * 4
}
df = pd.DataFrame(proyecciones)

st.header("📈 Proyecciones Trimestrales")
st.dataframe(df.style.format("{:,.0f}"))

# Cálculos mostrados
st.header("🧮 Detalles de los cálculos")
st.markdown(f'''
- **Costo total del financiamiento anual:** USD {costo_financiamiento:,.0f}  
- **Mejora proyectada en flujo de caja por reducción de cartera:** USD {mejora_caja:,.0f}  
- **Crecimiento estimado anual por uso de caja adicional:** USD {crecimiento_estimado:,.0f}
''')
