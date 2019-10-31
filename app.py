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

import webapi

from functools import wraps

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

            if username == 'marytan':
                session['custid'] = 2
                session['accountId'] = 74

            else:
                session['custid'] = 1
                session['accountId'] = 32
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
    number_of_acc = webapi.api_getListOfCreditAccounts(session['custid'])
    exp = expenditure()
    return render_template("dashboard.html", exp = exp)


# Dashboard
@app.route("/BankBalance")
def BankBalance():
    bank_balance = webapi.api_getAccountBalance(session['accountId'])
    return render_template("BankBalance.html", bank_balance = bank_balance)

# About
@app.route("/about")
@is_logged_in
def about():
    return render_template("about.html")


@app.route("/logout")
@is_logged_in
def logout():
    session.clear()
    return redirect(url_for("login"))



def expenditure():
    transaction_details = webapi.api_getTransactionDetails()
    exp = {}

    for i in transaction_details:
        if i['tag'] not in exp:
            exp[i['tag']] = 1
        else:
            exp[i['tag']] += 1

    return exp

if __name__ == "__main__":
    app.secret_key = "secret123"
    app.run(debug=True)
