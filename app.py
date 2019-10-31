from flask import (
    Flask,
    render_template,
    flash,
    redirect,
    url_for,
    session,
    request,
    logging,
)

app = Flask(__name__)

# Index
@app.route("/home")
def index():
    return render_template("home.html")

# Dashboard
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# About
@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)
