from flask import (
    Flask,
    render_template,
    redirect,
    url_for,
    session,
    request,
)
from functools import wraps
import webapi


app = Flask(__name__)

# simulate simple database
users = ["marytan", "limzeyang"]
passwords = ["1234", "5678"]

# Index, Login
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    userflag = False
    passflag = False
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        for user in users:
            if username == user:
                userflag = True
        for passes in passwords:
            if password == passes:
                passflag = True
        if userflag and passflag:
            session["logged_in"] = True
            session["username"] = username
            active_id = webapi.api_getUserID(username)
            session["custid"] = active_id

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
            return redirect(url_for("login"))

    return wrap

# Dashboard
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# About
@app.route("/profile")
@is_logged_in
def settings():
    print(session["custid"])
    return render_template(
        "profile.html",
        data=webapi.api_getCustomerDetails(session["custid"]),
        account=webapi.api_getListOfDepositAccounts(session["custid"]),
        credit=webapi.api_getListOfCreditAccounts(session["custid"]),
    )


@app.route("/logout")
@is_logged_in
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.secret_key = "secret123"
    app.run(debug=True)
