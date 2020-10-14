import requests #extremely common library for dealing w/ HTTP requests in python
import json #standard library for parsing JSON
from zappa.asynchronous import task #Zappa-specific magic to allow asynchronous tasks
from flask import Flask, request #our WSGI server

#Big Note! flask's `request` and the `requests` library are different, and both called in this app
#Life is an unending kafka-esque hellscape, I'm sorry.

#declaring that this app, this one right here? It's our Flask app
app = Flask(__name__)

@task #decorator that tells Zappa to run this asynchronously
def fetch_songs(response_url):
    #The URL is my endpoint, your slackbot will likely be hitting a different address
    songresponse = requests.get('https://wz3615f601.execute-api.us-east-2.amazonaws.com/prod')
    
    #turning the `text` attribute of this request into a Python object we can play with
    songjson = json.loads(songresponse.text)
    
    #immediately pulling the info out of `songjson` and building a message for slack with it
    textresponse = json.dumps({'text': f'*Your five Swift Songs are:*\n\n{songjson[0]}\n{songjson[1]}\n{songjson[2]}\n{songjson[3]}\n{songjson[4]}'})
    
    #using the response_url we passed into this function, we're now posting our response back to slack
    requests.post(response_url, data=textresponse)
    
    return ''

@app.route('/', methods=['POST']) #This can be any route with standard HTTP methods
def parse_command():
    #setting our local variable equal to the slack payload's parameter of the same name
    response_url = request.form.get('response_url')
    #then running that response url through fetch_songs()
    fetch_songs(response_url)
    #telling slack that we got the request within 3 seconds so they don't time out the request
    return 'Fetching songs...', 200