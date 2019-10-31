from flask import (
    Flask,
    render_template,
    flash,
    redirect,
    url_for,
    session,
    request,
    logging,
    request,
)
from functools import wraps
import webapi

app = Flask(__name__)


# Index, Login
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username != "" and password != "":
            session["logged_in"] = True
            session["username"] = username
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid Login"
            return render_template("login.html", error=error)

    return render_template("login.html")


def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Unauthorized, Please login", "danger")
            return redirect(url_for("login"))

    return wrap


# Dashboard
@app.route("/dashboard")
def dashboard():
    username = "marytan"
    customerId = webapi.api_getUserID(username)
    transactions = webapi.api_getTransactionDetails(customerId)
    expenses = {"Transport": 10, "F&B": 30, "Transfer": 40, "ATM": 20}
    transport = 40
    fnb = 30
    transfer = 20
    atm = 10
    return render_template("dashboard.html", transport=transport, fnb=fnb, transfer=transfer, atm=atm)


# About
@app.route("/about")
@is_logged_in
def about():
    return render_template("about.html")

@app.route('/api/ai_get_name/')
def api_get_name(name="Hello"):
    return json.jsonify({
        'name': name
    })

@app.route("/logout")
@is_logged_in
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.secret_key = "secret123"
    app.run(debug=True)
