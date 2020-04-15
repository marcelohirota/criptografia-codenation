import requests
import json

URL = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=token_do_usuario'

r = requests.get(URL).json()

with open('answer.json', 'w', encoding='utf-8') as f:
	json.dump(r, f, ensure_ascii=False, indent=4)