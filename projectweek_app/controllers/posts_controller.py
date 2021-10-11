from flask import render_template, request, session, redirect
from projectweek_app import app
from projectweek_app.models.User import User
from projectweek_app.models.Postu import Postu

from flask_bcrypt import Bcrypt

    ##################################### SEND POST ##################################

@app.route( "/home/post", methods = ['POST'] ) 
def sendPostu():
    posts_content = request.form['posts_content']
    user_id = request.form['users_id']

    data = (posts_content, user_id)

    print("FROM FORM 3 POSTU: ", data )
    print("END OF REGISTER PART", data)
    if Postu.validate_post(data):
        Postu.send_post(data)
    else:
        print("invalid values")
        return redirect('/home')
    print("END OF POST")
    return redirect('/home')

