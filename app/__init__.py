# -*- coding: utf-8 -*-

"""{Description}"""

__author__ = "k.mp"

# library imports
from flask import Flask

# project imports
from settings import Settings

# Initialize flask
app = Flask(__name__)
app.config.from_object(Settings)

# imports endpoints module
from app import routes
