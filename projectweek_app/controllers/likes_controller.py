from flask import render_template, request, session, redirect
from projectweek_app import app
from projectweek_app.models.User import User
from projectweek_app.models.Postu import Postu
from projectweek_app.models.Like import Like


@app.route('/home/post/like', methods = ['POST'])
def sendLikeDB():
    likes_count = request.form['likes_count']
    user_id = request.form['users_id']
    post_id = request.form['posts_id']

    data = ( likes_count, user_id, post_id )
    
    print("FROM FORM 4 LIKE: ", data )
    print("END OF SENDLIKE PART", data)
    result = Like.add_likes(data)
    print("LIKESSSSSSSSSS RESULT: ", result)
    return redirect('/home')