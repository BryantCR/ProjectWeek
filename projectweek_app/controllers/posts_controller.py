from flask import render_template, request, session, redirect
from projectweek_app import app
from projectweek_app.models.User import User
from flask_bcrypt import Bcrypt

@app.route( "/" ) #redirect allway to login
def redirectFirstPage():
    return redirect ('/login')

