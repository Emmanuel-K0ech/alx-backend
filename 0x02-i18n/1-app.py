#!/usr/bin/env python3
""" Flask i18n app """
from flask import Flask
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config():
    """ Class to hold LANGUAGES attribute """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@app.route("/")
def hello():
    """ flask route '/' """
    return "<title>Welcome to Holberton</title>"

# what does it mean to use Config to set Babel's default locale
# app.config.from_object(Config)
