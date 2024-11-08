#!/usr/bin/env python3
""" Flask i18n app """
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    """ flask route '/' """
    return "<title>Welcome to Holberton</title>"
