import streamlit as st
import json
from pathlib import Path

def afficher():
    st.subheader("📋 Indicateurs Cliniques Détectés")
    path = Path("data/indicateurs_complets.json")
    if path.exists():
        data = json.loads(path.read_text(encoding='utf-8'))
        for k, v in data.items():
            st.markdown(f"### {k.capitalize()}")
            st.markdown(f"**Modalité** : {v.get('modalité','?')}  ")
            st.markdown(f"**Troubles associés** : {', '.join(v.get('troubles_associés', []))}")
            st.markdown(f"**Explication** : {v.get('explication', '')}")