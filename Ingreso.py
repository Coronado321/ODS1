import numpy as np
import streamlit as st
import pandas as pd

st.write(''' # Predicción de ingreso mensual (USD)  ''')
st.image("ODS1imagen.jpg")

st.header('Datos')

def user_input_features():
  # Entrada
  añosesc = st.number_input('Años de escolaridad (decimal):', value = 0, step = 1)



  user_input_data = {'Años de escolaridad': añosesc}
  features = pd.DataFrame(user_input_data, index=[0])

  return features

df = user_input_features()

datos =  pd.read_csv('ods1_fin_pobreza.csv', encoding='latin-1')
X = datos.drop(columns='ingreso')
y = datos['ingreso']

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
LR = LinearRegression()
LR.fit(X_train,y_train)

b1 = LR.coef_
b0 = LR.intercept_
prediccion = b0 + b1[0]*df['Años de escolaridad']

st.subheader('Cálculo del ingreso mensual')
st.write('El ingreso de la persona es ', prediccion)
if prediccion < 215:
            st.warning("⚠️ Ingreso por debajo de la línea de pobreza extrema (~$2.15 USD/día · Banco Mundial)")
elif prediccion < 365:
            st.info("ℹ️ Ingreso cercano a la línea de pobreza moderada (~$3.65 USD/día · Banco Mundial)")
else:
            st.success("✅ Ingreso por encima de los umbrales de pobreza del Banco Mundial")
