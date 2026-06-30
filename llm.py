import os

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, Field
import instructor
from langfuse_client import langfuse

load_dotenv()

client = instructor.from_openai(
    OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
)

class RunnerData(BaseModel):
    plec: str | None = None
    wiek: int | None = None
    czas_5km_sek: int | None = None
    missing_fields: list[str] = Field(default_factory=list)

def parse_runner_data(user_message: str):    

    messages = [
            {
                "role": "system",
                "content": (
                    "Jesteś parserem danych, który wyciąga dane biegacza z tekstu. "
                    "Zwróć płeć (M lub K), wiek oraz czas na 5km w sekundach."
                    "Masz zwrócić WYŁĄCZNIE dane znajdujące się w tekście."
                    "Nigdy nie zgaduj brakujących informacji."
                    "Jeżeli którejś informacji brakuje, pozostaw odpowiednie pole puste i wpisz nazwę brakującego pola do missing_fields."
                )
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    
    trace = langfuse.trace(
        name="half-marathon-predicton",
        input=messages,
    )

    span = trace.span(
        name="runner-data-extraction",
        input={"user_message": user_message},
    )

    generation = span.generation(
        name="llm-parser",
        model="gpt-4.1-mini",
        input=messages,
    )

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        response_model=RunnerData,
        temperature=0,
        messages=messages,
    )

    generation.end(
        output=response.model_dump(),
    )

    langfuse.flush()

    
    return response
    
if __name__ == "__main__":

    runner = parse_runner_data(
        "Mam 30 lat, jestem mężczyzną i przebiegam 5 km w 25 minut"
    )

    print(runner)