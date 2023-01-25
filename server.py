from flask import Flask, request, render_template # can just use flask import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Chris is super poggers!</p>"

@app.route('/hi', methods=['GET']) # has to be methods
def hi(): # needs to have unique fxn name and import request
  user_name = request.args.get("userName", "unknown") # request.args is a dictionary
  return render_template('main.html', user=user_name) # render_template is imported and grabs an html template from /templates