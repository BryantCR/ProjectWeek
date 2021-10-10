from python_exam_app.config.MySQLConnection import connectToMySQL
from python_exam_app import app 
from datetime import date, datetime
from flask import flash
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, users_id, first_name, last_name, email, users_password, created_at):
        self.users_id = users_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.users_password = users_password
        self.created_at = created_at

    ################################################## INSERT USER DB ###################################

    @classmethod
    def user_Registration(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, users_password, created_at, updated_at) VALUES ( %(first_name)s , %(last_name)s , %(email)s, %(encryptedpassword)s, SYSDATE(), SYSDATE());"
        data2 = {
            "first_name" : data[0],
            "last_name" : data[1],
            "email" : data[2],
            "users_password" : data[3],
            "encryptedpassword" : data[4],
            "confirm_users_password" : data[5]
        }
        result = connectToMySQL('python_exam').query_db( query, data2 )
        print("RESULT LOGIN", result)
        return result
    
    ################################################## LOGIN ###################################

    @classmethod
    def user_login(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        data2 = {
            "email" : data[0],
            "users_password" : data[1],
        }
        result = connectToMySQL('python_exam').query_db( query, data2 )
        return result

    ################################################## GET ONE USER ###################################

    @classmethod
    def get_userBy_id( cls, data ):
        query = "SELECT * FROM users WHERE users_id = %(users_id)s;"
        results = connectToMySQL('python_exam').query_db( query, data )
        return results

    ################################################## GET ALL USERS ###################################

    @classmethod 
    def get_all_users( cls, data ):
        query = "SELECT * FROM users WHERE users_id != %(users_id)s ORDER BY first_name;"
        results = connectToMySQL('python_exam').query_db(query,data)
        print("RESULT GET ALL USERS MODEL", results)
        users = []
        for n in results:
            users.append( User( n['users_id'], n['first_name'], n['last_name'], n['email'], n['users_password'], n['created_at'] ) )
        return users

    ################################################## ????????????????? ###################################

    @classmethod
    def get_user_to_validate( cls, username ):
        query = "SELECT * FROM users WHERE username=%(username)s;"
        data = {
            "username" : username
        }
        result = connectToMySQL( "python_exam" ).query_db( query, data )
        return result

###################################################################### STATIC METHODS

    @staticmethod
    def validate_login( data ):
        is_valid = True
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!", "login")
            is_valid = False
        if len(data['users_password']) < 8:
            flash("Please enter a password. Passwords are at least 8 characters long", "login")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_registration(data):
        isValid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        data2 = {
            "first_name" : data[0],
            "last_name" : data[1],
            "email" : data[2],
            "users_password" : data[3],
            "encryptedpassword" : data[4],
            "confirm_users_password" : data[5]
        }
        results = connectToMySQL('python_exam').query_db( query, data2 )
        if len(results)>=1:
            flash("Email already registered")
            isValid = False
        if len( data[0] ) < 2:
            flash( "First name must be at least 2 characters long" )
            isValid = False 
        if len( data[1] ) < 2:
            flash( "Last name must be at least 2 characters long")
            isValid = False
        if not EMAIL_REGEX.match(data[2]):
            flash("Email Address must have a valid format, try with a new one please")
            isValid = False
        if len(data[3]) < 8:
            flash("Password must be at least 8 characters long")
            isValid = False
        if data[3] != data[5]:
            flash("Passwords must match, try again")
            isValid = False
        if len(data[0]) == 0 or len(data[1]) == 0 or len(data[2]) == 0 or len(data[3]) == 0 or len(data[4]) == 0:
            flash("There is an empty data space try to fill it")
            isValid = False
        return isValid

#####################################################################################################################################
