#!/usr/bin/env python3
""" Flask i18n app """
from flask import Flask, request
from flask_babel import Babel


@babel.localselector
def get_locale():
    """ Determines the best match with our supported languages"""
    return request.accept_language.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
babel = Babel(app, localselector=get_locale)
