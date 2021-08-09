

from flask import Flask, render_template, redirect, request, url_for
from functions import *

app = Flask(__name__)

@app.route("/auth/login")
def login():
	return "Hello World!"

@app.route("/auth/signup")
def signup():
	return "Hello World2!"

if __name__ == "__main__":
	app.run()