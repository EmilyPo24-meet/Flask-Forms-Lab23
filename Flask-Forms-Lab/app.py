from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "siwarha"
password = "123"
facebook_friends=["hila","keren","alma", "noam", "sashawithanalef"]



@app.route('/', methods=['GET','POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		user = request.form['username']
		passw = request.form['password']
		if user == username and passw == password:
			return render_template('home.html', u = username, p = password,list=facebook_friends)
		else:
			return render_template('login.html')

@app.route('/home')  # '/' for the default page
def home():
	return render_template('home.html')
			# return render_template('home.html', u = username, p = password)

@app.route('/friend_exists/<string:name>')
def friendex(name):
	name_in = ""
	if name in facebook_friends:
		name_in = "true"
		return render_template('friend_exists.html', e = name_in)


	else:
		name_in = "false"
		return render_template('friend_exists.html', e = name_in)

  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
