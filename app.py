import streamlit as st

from llm import parse_runner_data
from predictor import load_model
from utils import predict_halfmarathon_time
from langfuse_client import langfuse

@st.cache_resource
def get_model():
    return load_model()

        
model = get_model()


FIELD_NAMES = {
        "plec": "płeć",
        "wiek": "wiek",
        "czas_5km_sek": "czas na 5 km"
    }


st.set_page_config(page_title="Half Marathon Predictor")

st.title("🏃 Half Marathon Predictor")

st.write(
    "Podaj swoją płeć, wiek oraz czas na 5 km, a AI oszacuje Twój czas ukończenia półmaratonu."
)

user_message = st.text_area(
    "Opisz biegacza",
    placeholder="Np. Mam 32 lata, jestem mężczyzną i mój czas na 5 km to 24 minuty."
)

if st.button("Przewiduj"):

    trace = langfuse.trace(
        name="half-marathon-prediction"
    )

    runner = parse_runner_data(user_message)

    if runner.missing_fields:
        st.error("Podaj więcej informacji:")

        st.markdown(
            "\n".join(
                f"- {FIELD_NAMES.get(field, field)}"
                for field in runner.missing_fields
            )
        )
        st.stop()


    pred_seconds, pred_time = predict_halfmarathon_time(
        model=model,
        plec=runner.plec,
        wiek=runner.wiek,
        czas_5km_sek=runner.czas_5km_sek
    )

    st.write(f"Płeć: {runner.plec}")
    st.write(f"Wiek: {runner.wiek}")
    st.write(f"Czas na 5 km: {runner.czas_5km_sek} sek")

    st.success(f"🏁 Przewidywany czas: {pred_time}")

    trace.update(
        output={
            "prediction": pred_time,
            "age": runner.wiek,
            "gender": runner.plec,
            "time_5km_seconds": runner.czas_5km_sek,
        }
    )

    langfuse.flush()

    