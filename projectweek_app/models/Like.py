from projectweek_app.config.MySQLConnection import connectToMySQL
from projectweek_app import app 
from datetime import date, datetime
from flask import flash
import re

class Like:
    def __init__(self, likes_id, user_id, post_id, likes, created_at, updated_at):
        self.likes_id = likes_id
        self.user_id = user_id
        self.post_id = post_id
        self.likes = likes
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def add_likes( cls, data ):
        # query = "INSERT INTO likes (user_id, post_id, likes, created_at, updated_at) VALUES ( %(user_id)s, %(post_id)s, %(likes)s, SYSDATE(), SYSDATE());"
        # data2 = {
        #     "user_id" : data[1],
        #     "post_id" : data[2],
        #     "likes" : data[0]
        # }
        # result2 = connectToMySQL('project_app').query_db( query, data2 )

        query = "UPDATE posts SET post_likes = post_likes +1 WHERE posts_id = %(post_id)s;"
        data3 = {
            "user_id" : data[1],
            "post_id" : data[2],
            "post_likes" : data[0]
        }
        result = connectToMySQL('project_app').query_db( query, data3 )
        print("RESULT SEND LIKE DB: ", result)
        return result
        # user = []
        # for n in result:
        #     user.append( Like( n['likes_id'], n['user_id'], n['post_id'], n['likes_count'] ) )
        # return user


#select likes, target post_likes, +1 test 2