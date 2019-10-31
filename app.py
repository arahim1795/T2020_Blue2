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
            return redirect(url_for("about"))
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


if __name__ == "__main__":
    app.secret_key = "secret123"
    app.run(debug=True)
