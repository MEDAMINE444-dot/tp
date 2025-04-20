import streamlit as st
import pandas as pd
st.title("Bienvenue sur l'application Qualité des Données 📊")
st.write("Utilisez le menu à gauche pour naviguer entre les pages.")


st.title("🔐 Page de connexion")

username = st.text_input("Nom d'utilisateur")
password = st.text_input("Mot de passe", type="password")

if st.button("Se connecter"):
    if username == "admin" and password == "1234":
        st.success("Connexion réussie ✅")
    else:
        st.error("Identifiants incorrects ❌")


st.title("📊 Dashboard Qualité des Données")

# Chargement des données
data = pd.read_csv("vente.csv")

# Calculs KPI
taux_complet = data['CustomerID'].notnull().mean() * 100
nb_anomalies = len(data[(data['Price'] < 0) | (data['Price'] > 1000)])
delai_moyen = (pd.to_datetime("today") - pd.to_datetime(data['Last_Update'], errors='coerce')).dt.days.mean()

# KPI affichés
st.metric("📝 Taux de complétude CustomerID", f"{taux_complet:.2f} %")
st.metric("⚠️ Anomalies de prix", f"{nb_anomalies}")
st.metric("⏳ Ancienneté moyenne des données", f"{delai_moyen:.0f} jours")
