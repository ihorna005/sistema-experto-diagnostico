import streamlit as st

def diagnose_covid(symptoms):
    if symptoms.get('fever') and symptoms.get('cough') and symptoms.get('loss_of_taste'):
        if symptoms.get('breathing_difficulty'):
            return "🔴 Alto riesgo de COVID-19. Se recomienda prueba PCR y atención médica urgente."
        else:
            return "🟠 Posible caso de COVID-19. Se recomienda aislamiento y realizar una prueba."
    elif symptoms.get('fever') and symptoms.get('cough'):
        return "🟡 Síntomas compatibles con COVID-19 o gripe. Observe evolución y considere test."
    elif symptoms.get('loss_of_taste'):
        return "🟡 Pérdida de gusto/olfato detectada. Posible COVID-19. Se sugiere prueba."
    else:
        return "🟢 Síntomas no concluyentes para COVID-19. Monitoreo recomendado."

# Streamlit UI
st.set_page_config(page_title="Diagnóstico de COVID-19", page_icon="🧪")

st.title("🧠 Sistema Experto para Diagnóstico de COVID-19")
st.markdown("Por favor, seleccione los síntomas presentes:")

fever = st.checkbox("Fiebre")
cough = st.checkbox("Tos")
fatigue = st.checkbox("Fatiga")
loss_of_taste = st.checkbox("Pérdida del gusto o del olfato")
breathing_difficulty = st.checkbox("Dificultad para respirar")

if st.button("Diagnosticar"):
    symptoms = {
        'fever': fever,
        'cough': cough,
        'fatigue': fatigue,
        'loss_of_taste': loss_of_taste,
        'breathing_difficulty': breathing_difficulty
    }
    result = diagnose_covid(symptoms)
    st.subheader("🩺 Resultado del Diagnóstico")
    st.success(result) if "🟢" in result else st.warning(result) if "🟡" in result else st.error(result)

#    st.success(result) if \"🟢\" in result else st.warning(result) if \"🟡\" in result else st.error(result)

