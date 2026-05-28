import requests
import json
import os


API_KEY = os.getenv("OPENROUTER_API_KEY")


def predict_health(glucose, haemoglobin, cholesterol):

    prompt = f"""
    Analyze these blood test results.

    Glucose: {glucose}
    Haemoglobin: {haemoglobin}
    Cholesterol: {cholesterol}

    Predict possible health risk or disease in one short sentence only.
    """

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        })
    )

    result = response.json()

    return result["choices"][0]["message"]["content"]