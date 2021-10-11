from projectweek_app.config.MySQLConnection import connectToMySQL
from projectweek_app import app 
from datetime import date, datetime
from flask import flash
import re

class Like:
    def __init__(self, likes_id, user_id, post_id, likes_count, created_at, updated_at):
        self.likes_id = likes_id
        self.user_id = user_id
        self.post_id = post_id
        self.likes_count = likes_count
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def add_likes( cls, data ):
        query = "INSERT INTO likes (user_id, post_id, likes_count, created_at, updated_at) VALUES ( %(user_id)s, %(post_id)s, %(likes_count)s, SYSDATE(), SYSDATE());"
        data2 = {
            "user_id" : data[1],
            "post_id" : data[2],
            "likes_count" : data[0]
        }
        result = connectToMySQL('project_app').query_db( query, data2 )
        print("RESULT SEND LIKE DB: ", result)
        return result



