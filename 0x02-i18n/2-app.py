#!/usr/bin/env python3
""" Flask i18n app """
from flask import Flask, request
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


@babel.localselector
def get_locale():
    """ Determines the best match with our supported languages"""
    return request.accept_language.best_match(app.config['LANGUAGES'])
