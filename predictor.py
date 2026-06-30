#importy
import os
import joblib
import boto3

from dotenv import load_dotenv
from pathlib import Path

#zmienne srodowiskowe
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / "models"

DO_SPACES_KEY = os.getenv("DO_SPACES_KEY")
DO_SPACES_SECRET = os.getenv("DO_SPACES_SECRET")
DO_SPACES_REGION = os.getenv("DO_SPACES_REGION")
DO_SPACES_BUCKET = os.getenv("DO_SPACES_BUCKET")
DO_SPACES_ENDPOINT = os.getenv("DO_SPACES_ENDPOINT")

#klient s3
s3 = boto3.client(
    "s3",
    region_name=DO_SPACES_REGION,
     endpoint_url=DO_SPACES_ENDPOINT,
     aws_access_key_id=DO_SPACES_KEY,
     aws_secret_access_key=DO_SPACES_SECRET,
)

def load_model():
    """
    Pobiera model z DigitalOcean Spaces i zwraca załadowany model.
    """

    MODELS_DIR.mkdir(parents=True, exist_ok=True)

    model_path = MODELS_DIR / "halfmarathon_linear_regression.pkl"
    
    s3.download_file(
        Bucket=DO_SPACES_BUCKET,
        Key="models/halfmarathon_linear_regression.pkl",
        Filename=model_path,
    )

    model = joblib.load(model_path)

    return model

#if __name__ == "__main__":
    #model = load_model()
    #print(type(model))

