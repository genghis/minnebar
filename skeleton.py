from flask import Flask, request #our WSGI server

#declaring that this app, this one right here? It's our Flask app
app = Flask(__name__) 

@app.route('/', methods=['POST']) #This can be any route with standard HTTP methods
def parse_command():
	#setting our local variable equal to the slack payload's parameter of the same name
    response_url = request.form.get('response_url') 
    #returning that URL
    return response_url, 200