from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret-key"

@app.context_processor
def inject_year():
    return {"year": datetime.now().year}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    if not (name and email and message):
        flash("Please fill out all fields!", "error")
        return redirect(url_for("index") + "#contact")

    flash("Thank you! Your message has been received.", "success")
    return redirect(url_for("index") + "#contact")

if __name__ == "__main__":
    app.run(debug=True)
