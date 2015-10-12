from flask import Flask
from flask import request
from flask import abort
from flask import redirect
from flask import *  ##load_user



app = Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello World!</h1><br> <h2>yoooo</h2>'

@app.route('/user/<id>')
def get_user(id):
	user = load_user(id)
	if not user:
		abort(404)
	return '<h1>Hello, %s</h1>' % user.name

@app.route('/browser')
def browser():
	user_agent = request.headers.get('User-Agent')
	return '<p>Your browser is %s</p>' % user_agent

@app.route('/duck')
def duck():
	return redirect('http://www.duckduckgo.com')

if __name__ == '__main__':
	app.run(debug = True)

