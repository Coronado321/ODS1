# Importar librerías necearias
import numpy as np
import streamlit as st
import pandas as pd

# Insertamos título
st.write(''' # ODS 1: Fin de la pobreza ''')
# Insertamos texto con formato
st.markdown("""
Esta aplicación utiliza **Machine Learning** para predecir el ongreso mensual segun los años de escolaridad, alineado con el **ODS 1**.
""")
# Insertamos una imagen
st.image("ODS1imagen.jpg")



# Definimos cómo ingresará los datos el usuario
# Usaremos un deslizador
st.sidebar.header("Parámetro personal")
# Definimos los parámetros de nuestro deslizador:

temp_input = st.sidebar.slider("Años escolaridad", 0, 70)

# Cargamos el archivo con los datos (.csv)
df =  pd.read_csv('ods1_fin_pobreza.csv', encoding='latin-1')
# Seleccionamos las variables
X = df[['anos_escolaridad']]
y = df['ingreso_mensual_usd']

# Creamos y entrenamos el modelo
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)
LR = LinearRegression()
LR.fit(X_train,y_train)

# Hacemos la predicción con el modelo y la temperatura seleccionada por el usuario
b1 = LR.coef_
b0 = LR.intercept_
prediccion = b0 + b1[0]*temp_input

# Presentamos loa resultados
st.subheader('ingreso mensual')
st.write(f'El ingreso mensual en dolares es de: {prediccion}')

if prediccion < 215:
            st.warning("⚠️ Ingreso por debajo de la línea de pobreza extrema (~$2.15 USD/día · Banco Mundial)")
elif prediccion < 365:
            st.info("ℹ️ Ingreso cercano a la línea de pobreza moderada (~$3.65 USD/día · Banco Mundial)")
else:
            st.success("✅ Ingreso por encima de los umbrales de pobreza del Banco Mundial")
