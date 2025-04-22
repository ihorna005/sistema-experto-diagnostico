import streamlit as st

# Título
st.title("🩺 Sistema Experto de Diagnóstico de Enfermedades Respiratorias")

# Instrucciones
st.markdown("Selecciona los síntomas que estás experimentando:")

# Lista de síntomas
sintomas = {
    "Fiebre": st.checkbox("Fiebre"),
    "Tos seca": st.checkbox("Tos seca"),
    "Dolor de garganta": st.checkbox("Dolor de garganta"),
    "Congestión nasal": st.checkbox("Congestión nasal"),
    "Fatiga": st.checkbox("Fatiga"),
    "Pérdida del olfato/gusto": st.checkbox("Pérdida del olfato/gusto"),
    "Dolor muscular": st.checkbox("Dolor muscular"),
    "Estornudos": st.checkbox("Estornudos")
}

# Diagnóstico
diagnostico = ""
color = "white"
recomendacion = ""
reglas_activadas = []

# Reglas de diagnóstico
if sintomas["Fiebre"] and sintomas["Tos seca"] and sintomas["Fatiga"] and sintomas["Pérdida del olfato/gusto"]:
    diagnostico = "Probable COVID-19"
    color = "red"
    recomendacion = "Aíslate y hazte una prueba COVID-19."
    reglas_activadas.append("Fiebre + Tos seca + Fatiga + Pérdida del olfato/gusto")

elif sintomas["Fiebre"] and sintomas["Dolor muscular"] and sintomas["Fatiga"] and sintomas["Tos seca"]:
    diagnostico = "Posible Gripe"
    color = "orange"
    recomendacion = "Descansa y consulta al médico si los síntomas persisten."
    reglas_activadas.append("Fiebre + Dolor muscular + Fatiga + Tos seca")

elif sintomas["Congestión nasal"] and sintomas["Estornudos"] and sintomas["Dolor de garganta"]:
    diagnostico = "Resfriado Común"
    color = "green"
    recomendacion = "Mantente hidratado y descansa."
    reglas_activadas.append("Congestión nasal + Estornudos + Dolor de garganta")

else:
    diagnostico = "Síntomas no concluyentes"
    color = "gray"
    recomendacion = "Consulta a un profesional médico para un diagnóstico preciso."

# Mostrar diagnóstico
st.markdown(f"### 🧾 Diagnóstico: <span style='color:{color}'>{diagnostico}</span>", unsafe_allow_html=True)
st.markdown(f"### 💡 Recomendación: <span style='color:{color}'>{recomendacion}</span>", unsafe_allow_html=True)

# Mostrar reglas activadas
if reglas_activadas:
    with st.expander("Ver reglas activadas"):
        for regla in reglas_activadas:
            st.markdown(f"- {regla}")
