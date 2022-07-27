import requests
params_api = {
    'amount': 10,
    'type': 'boolean'
}
resp = requests.get(url='https://opentdb.com/api.php', params=params_api)
resp.raise_for_status()
data = resp.json()
question_data = data['results']
