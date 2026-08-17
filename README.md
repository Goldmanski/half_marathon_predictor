# 🏃 Half Marathon Predictor

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4.1--Mini-green)
![Langfuse](https://img.shields.io/badge/Langfuse-Observability-orange)
![Scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E)

AI-powered application that predicts half marathon finish time based on natural language input using a Machine Learning model and an LLM.

## 📷 Preview

![Half Marathon Predictor](screenshots/app.png)

## 📌 Project Overview

Half Marathon Predictor is an AI application that predicts a runner's half marathon finish time based on natural language input.

The application combines:

- Machine Learning for time prediction
- OpenAI GPT-4.1 Mini for extracting structured data from free text
- Instructor and Pydantic for structured LLM outputs
- Langfuse for monitoring LLM calls
- Streamlit as the user interface

The trained regression model is included directly in the repository and loaded locally by the application.

## 🚀 Features

- Predict half marathon finish time
- Accept natural language input
- Extract runner data from natural language using GPT
- Validate missing information
- Use a locally stored trained regression model
- Monitor LLM calls with Langfuse
- Deploy the application using Streamlit Community Cloud

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Streamlit
- Scikit-learn
- OpenAI API
- Instructor
- Pydantic
- Langfuse
- Joblib

## 🏗 Architecture

                    User
                      │
                      ▼
            Streamlit Application
                      │
                      ▼
     OpenAI GPT-4.1 Mini + Instructor
                      │
                      ▼
      Structured Runner Information
                      │
                      ▼
          Local Regression Model
                      │
                      ▼
     Predicted Half Marathon Time

The trained model is stored in the `models/` directory and loaded locally using `joblib`.

## 📁 Project Structure

    half_marathon_predictor/
    │
    ├── app.py                  # Streamlit application
    ├── llm.py                  # LLM-based data extraction
    ├── predictor.py            # Loads the trained model
    ├── utils.py                # Prediction utilities
    ├── langfuse_client.py      # Langfuse configuration
    ├── requirements.txt
    │
    ├── data/
    │   ├── halfmarathon_wroclaw_2023_final.csv
    │   └── halfmarathon_wroclaw_2024_final.csv
    │
    ├── models/
    │   └── halfmarathon_linear_regression.pkl
    │
    ├── screenshots/
    │
    └── README.md

## ⚙️ How It Works

1. The user enters a natural language description.
2. GPT extracts:
   - gender
   - age
   - 5 km time
3. The application validates the extracted information.
4. The trained regression model predicts the half marathon finish time.
5. The prediction is displayed in the Streamlit interface.
6. Langfuse monitors the LLM interaction.

## 💬 Example

### Input

> I am a 28-year-old male and my 5 km time is 22 minutes.

### Output

    Predicted half marathon time:
    01:43:58

### Missing Information

Input:

> I am a 28-year-old male.

Output:

    Missing information:

    - 5 km time

## 📊 LLM Monitoring

The application uses Langfuse to monitor LLM interactions, including:

- prompts
- model responses
- model information
- execution traces

This provides visibility into the LLM-based data extraction process.

![Langfuse Monitoring](screenshots/langfuse.png)

## ☁️ Deployment

The application is deployed using Streamlit Community Cloud.

The trained machine learning model is included in the GitHub repository and loaded locally by the application.

API keys and other sensitive configuration are provided through Streamlit Community Cloud Secrets and are not stored in the repository.

## 🔮 Future Improvements

- Support additional race distances
- Compare multiple prediction models
- Store prediction history
- User authentication
- REST API version

## 📄 License

This project is available for educational and portfolio purposes.

## 👨‍💻 Author

Eliasz Nowicki

GitHub: **@Goldmanski**