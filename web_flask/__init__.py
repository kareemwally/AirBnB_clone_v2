#!/usr/bin/python3
"""
the __init__ file for the apps in the project
"""
from flask import Flask, render_template
def create_app(config_name):
    """ creating a new app """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    return app
