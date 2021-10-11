from flask import Flask, render_template, request, redirect, session
from projectweek_app import app
from projectweek_app.controllers import users_controller
from projectweek_app.controllers import posts_controller
from projectweek_app.controllers import likes_controller


#from projectweek_app.controllers import 

if __name__ == "__main__":
    app.run( debug = True )


