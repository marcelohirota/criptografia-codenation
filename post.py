import requests
import json

def send_form():
    POST = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=token_do_usuario"
    answer = {'answer': open('answer.json', 'rb')}
    submit = requests.post(POST, files=answer)
    print(submit.headers)

send_form()