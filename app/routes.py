# -*- coding: utf-8 -*-

"""{Description}"""

__author__ = "k.mp"

# library imports imports
from flask import render_template

# project imports
from app import app


@app.route("/")
def home():
    posts = None
    return render_template("index.html", posts=posts)


@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/tutorial")
def tutorial():
    return render_template("tutorial.html")


@app.route("/test")
def test():
    return render_template("generated/test2.html")