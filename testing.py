import requests
import json
from zappa.asynchronous import task
from flask import Flask, request

app = Flask(__name__)

@task
def fetch_songs(response_url):
    songresponse = requests.get('https://wz3615f601.execute-api.us-east-2.amazonaws.com/prod')
    songjson = json.loads(songresponse.text)
    textresponse = json.dumps({'text': f'*Your five Swift Songs are:*\n\n{songjson[0]}\n{songjson[1]}\n{songjson[2]}\n{songjson[3]}\n{songjson[4]}'})
    print(textresponse)
    # requests.post(response_url, data=textresponse)
    return ''

@app.route('/', methods=['POST'])
def parse_command():
    response_url = request.form.get('response_url')
    print(f'RESPONSE URL IS: {response_url}')
    fetch_songs(response_url)
    return 'Fetching songs...', 200