import pandas as pd

def seconds_to_hhmmss(total_seconds):
    total_seconds = int(round(total_seconds))

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    return f"{hours:02}:{minutes:02}:{seconds:02}"


def predict_halfmarathon_time(model, plec, wiek, czas_5km_sek):
    """
    Przewiduje czas ukończenia półmaratonu
    """

    plec_map = {
        "M": 1,
        "K": 0,
    }

    input_df = pd.DataFrame({
        "Płeć": [plec_map[plec]],
        "Wiek": [wiek],
        "5 km Czas sek": [czas_5km_sek]
    })

    predicted_seconds = model.predict(input_df)[0]

    predicted_time = seconds_to_hhmmss(predicted_seconds)

    return predicted_seconds, predicted_time