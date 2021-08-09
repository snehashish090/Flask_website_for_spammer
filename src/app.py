
from flask import Flask, render_template, redirect, request, url_for
from functions import *
from flask_mail import Mail
from flask_mail import Message

app = Flask(__name__)
mail = Mail(app)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = "snehashish.laskar@sahyadrischool.org"
app.config['MAIL_PASSWORD'] = 'snehashish08036'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/", methods=["GET", "POST"])
def landing_page():
	if request.method == "POST":
		rec = request.form["rec"]
		sen = request.form["sen"]
		pw = request.form["pw"]

		msg = Message("Hi my name is {}".format(rec),
				sender= sen,
				recipients = [rec]
			)
		msg.body = "Hi my name is Snehashish"
		mail.send(msg)
		return "DOne!"
	else:
		return render_template("landing_page.html")

if __name__ == "__main__":
	app.run(debug=True)