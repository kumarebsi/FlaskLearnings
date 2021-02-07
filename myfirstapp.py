from flask import Flask, render_template, request, url_for, redirect, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "8778"
app.permanent_session_lifetime = timedelta(days=5)

@app.route("/")
def home():
	return redirect(url_for("login"))

@app.route("/login", methods = ["POST","GET"])
def login():
	if request.method=="POST" and "user" not in session:
		session["user"] = request.form["usr"]
		return redirect(url_for("user"))
	elif "user" in session:
		return redirect(url_for("user"))
	else:
		return render_template("index.html")

@app.route("/user/", methods=["POST","GET"])
def user():
	if request.method == "POST":
		session.pop("user")
		return redirect(url_for("login"))
	user=session["user"]
	return render_template("user.html", user=user)


if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
