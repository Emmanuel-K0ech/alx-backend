#!/usr/bin/env python3
""" Flask i18n app """
from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
babel = Babel()


class Config():
    """ Class to hold LANGUAGES attribute """
    LANGUAGES = ["en", "fr"]


@app.route("/")
def hello() -> str:
    return "<h1>Hello world</h1>"
