import streamlit as st
from modules import visuel, audio, posture, indicateurs

st.set_page_config(page_title='PsyAI', layout='wide')
st.title('🧠 PsyAI – Analyse clinique assistée par IA')

menu = st.sidebar.radio("Navigation", ["Accueil", "Observation Visuelle", "Analyse Vocale", "Langage Corporel", "Indicateurs Cliniques"])

if menu == "Observation Visuelle":
    visuel.afficher()
elif menu == "Analyse Vocale":
    audio.afficher()
elif menu == "Langage Corporel":
    posture.afficher()
elif menu == "Indicateurs Cliniques":
    indicateurs.afficher()
else:
    st.write("Bienvenue dans PsyAI")