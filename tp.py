
import streamlit as st
import pandas as pd
import datetime

# Chargement des données (exemple CSV)
data = pd.read_csv("ventes.csv")

# Calculs
today = pd.to_datetime("today")

# Complétude CustomerID
taux_complet = data['CustomerID'].notnull().mean() * 100

# Anomalies de prix (<0 ou >1000)
anomalies = data[(data['Price'] < 0) | (data['Price'] > 1000)]
nb_anomalies = len(anomalies)

# Ancienneté moyenne des mises à jour
data['Last_Update'] = pd.to_datetime(data['Last_Update'], errors='coerce')
data['Delai'] = (today - data['Last_Update']).dt.days
delai_moyen = data['Delai'].mean()

# Type d'anomalie
data['Anomalie'] = data['Price'].apply(lambda x: "Prix Douteux" if x < 0 or x > 1000 else "Normal")

# Interface Streamlit
st.title("📊 Dashboard Qualité des Données")

# Indicateurs KPI
st.metric("Taux de complétude CustomerID", f"{taux_complet:.2f} %")
st.metric("Nombre d'anomalies de prix", f"{nb_anomalies}")
st.metric("Ancienneté moyenne des données", f"{delai_moyen:.0f} jours")

# Histogramme des ventes douteuses
st.subheader("Histogramme des ventes par type")
st.bar_chart(data['Anomalie'].value_counts())

# Affichage des anomalies détaillées
st.subheader("📄 Détails des anomalies de prix")
st.dataframe(anomalies)

# Footer
st.write("👨‍💻 Dashboard réalisé avec Streamlit & Python")
