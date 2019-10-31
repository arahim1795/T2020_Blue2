from flask import (
    Flask,
    render_template,
    flash,
    redirect,
    url_for,
    session,
    request,
    logging,
    Response,
    Request
)

import json
import requests


def api_getUserID(username=None):
    api_headers = {'identity': 'Group2', 'token': '2c55f846-e723-4564-b93c-35630007dd7a'}
    if username is None:
        api_url = 'http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/customers/marytan'
    else:
        api_url = 'http://techtrek-api-gateway.ap-southeast-1.elasticbeanstalk.com/customers/' + username
    response = requests.get(api_url, headers=api_headers)

    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        return data["customerId"]
    else:
        return None

app = Flask(__name__)


# Index
@app.route("/")
def index():
    return render_template("home.html")


# About
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
