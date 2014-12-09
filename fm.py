#!/usr/bin/env python
# encoding: utf-8
from flask import Flask
from flask.ext.restful import Api
from flask import render_template
from config import url_map
from config.config import SECRET_KEY

app = Flask(__name__)
api = Api(app)

app.jinja_env.variable_start_string = '[['
app.jinja_env.variable_end_string = ']]'
app.secret_key = SECRET_KEY

url_map.set_url_map(api)

app.debug = True
@app.route('/')
def index():
    return render_template("index.html")
