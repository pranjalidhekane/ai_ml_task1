import requests
import json
import os

API_KEY = os.getenv("OPENROUTER_API_KEY")


def local_prediction(glucose, haemoglobin, cholesterol):
    if glucose > 140 and cholesterol > 240:
        return "Possible diabetes and cardiovascular risk detected."
    elif glucose > 140:
        return "Possible diabetes risk detected."
    elif cholesterol > 240:
        return "Possible cardiovascular risk detected."
    elif haemoglobin < 12:
        return "Possible anemia risk detected."
    else:
        return "No major risk detected based on given values."


def predict_health(glucose, haemoglobin, cholesterol):

    if not API_KEY:
        return local_prediction(glucose, haemoglobin, cholesterol)

    prompt = f"""
    Analyze these blood test results:
    Glucose: {glucose}
    Haemoglobin: {haemoglobin}
    Cholesterol: {cholesterol}

    Predict possible health risk in one short sentence.
    """

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "model": "openai/gpt-4o-mini",
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }),
            timeout=20
        )

        result = response.json()

        if "choices" in result:
            return result["choices"][0]["message"]["content"]

        return local_prediction(glucose, haemoglobin, cholesterol)

    except Exception:
        return local_prediction(glucose, haemoglobin, cholesterol)