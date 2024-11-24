import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Título 
st.title("Tabla de amortización")

# Entrada de datos por el usuario
monto = st.number_input("Ingrese el monto del préstamo:", min_value=0.0, format="%f")
periodos = st.number_input("Ingrese el número de periodos:", min_value=1, format="%d")
interes = st.number_input("Ingrese la tasa de interés:", min_value=0.0, format="%f") / 100

if monto > 0 and periodos > 0 and interes > 0:
    cuota = (monto * interes) / (1 - (1 + interes) ** -periodos)
    st.write("Usted está solicitando una amortización con las siguientes condiciones:")
    st.write(f"Un monto de: ${monto}")
    st.write(f"Por {periodos} periodos")
    st.write(f"Con una tasa de interés de: {interes * 100}%")
    st.write(f"**El pago periódico del crédito es: ${cuota:.2f}**")

    
    saldo = monto
    amortizacion = []

    # Generador de tabla de amortización con iteradores
    for i in range(periodos + 1):
        if i == 0:
            amortizacion.append([i, 0, 0, 0, saldo])
        else:
            interes_mensual = saldo * interes
            capital = cuota - interes_mensual
            saldo -= capital
            amortizacion.append([i, cuota, interes_mensual, capital, saldo])

    # Convertir a DataFrame para visualización
    df_amortizacion = pd.DataFrame(amortizacion, columns=["Periodo", "Cuota", "Intereses", "Capital", "Saldo"])

    # Mostrar tabla de amortización
    st.write("### Tabla de Amortización")
    st.dataframe(df_amortizacion)

    # Graficar la tabla de amortización
    st.write("### Gráfica de Amortización")
    fig, ax = plt.subplots()
    ax.plot(df_amortizacion["Periodo"], df_amortizacion["Saldo"], marker='o')
    ax.set_xlabel("Periodo")
    ax.set_ylabel("Saldo")
    ax.set_title("Saldo del Préstamo por Periodo")
    st.pyplot(fig)
else:
    st.write("Por favor, ingrese valores positivos para el monto, los periodos y la tasa de interés.")
