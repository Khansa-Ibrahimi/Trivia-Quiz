import requests

# Parameters for the API call to get 10 True/False questions
parameters = {
    "amount": 10,
    "type": "boolean"
}

# Make a GET request to the Open Trivia DB API
response = requests.get("https://opentdb.com/api.php?", params=parameters)
response.raise_for_status()

data = response.json()

# Extract the list of questions
question_data = data["results"]
