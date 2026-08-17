import joblib
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"


def load_model():
    """
    Ładuje model lokalnie i zwraca załadowany model.
    """

    model_path = MODELS_DIR / "halfmarathon_linear_regression.pkl"

    model = joblib.load(model_path)

    return model

