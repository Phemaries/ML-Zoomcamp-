import requests

url = 'http://localhost:9696/predict'

# client = {"job": "unknown", "duration": 270, "poutcome": "failure"}

client = {"job": "retired", "duration": 445, "poutcome": "success"}

response = requests.post(url, json=client).json()

print(response)

# {'churn_probability': 0.13968947052356817}
