











#========================================================================================#


# from flask import render_template, request, redirect, session
# from python_exam_app import app
# from python_exam_app.models.User import User
# from python_exam_app.models.Car import Car
# from flask_bcrypt import Bcrypt


# bcrypt = Bcrypt(app)

# @app.route( "/" ) #redirect allway to home
# def displayLoginWall():
#     return redirect ('/login')

# @app.route( "/login", methods = ['GET'] )#Home page
# def displayLoginRegistration():
#     return render_template( "loginwall.html")

# @app.route('/login/register', methods = ['POST'] )#receive the data an does the registration
# def registerUser():
#     first_name = request.form['first_name']
#     last_name = request.form['last_name']
#     email = request.form['email']
#     users_password = request.form['users_password']
#     encryptedpassword = bcrypt.generate_password_hash(users_password)
#     confirm_users_password = request.form['confirm_users_password']

#     data = (first_name,last_name,email,users_password,encryptedpassword,confirm_users_password)
#     print("FROM FORM 1 REGISTER: ", data )
#     print("END OF REGISTER PART", data)
#     if User.validate_registration(data):
#         User.register_login(data)
#     else:
#         print("invalid values")
#     return redirect('/login')

# @app.route('/login/user', methods = ['POST'] )#receive the data from DB and redirects to the private wall
# def userlogin():
#     email = request.form['email']
#     users_password = request.form['users_password']
#     data = (email, users_password)
#     result  = User.user_login(data)
#     if len( result ) > 0:
#         encryptedPassword = result[0]['users_password']
#         print(encryptedPassword)
#         if bcrypt.check_password_hash( encryptedPassword, users_password ):
#             session.clear()
#             users_id = result[0]['users_id']
#             session['users_id'] = users_id
#             return redirect ('/dashboard')
#         else:
#             messageWrongPass = "Wrong credentials provided."
#             session['ErrorMessage'] = messageWrongPass
#     else:
#         messageWrongPass = "There is no user with this information"
#         session['ErrorMessage'] = messageWrongPass
#     return redirect('/login')

# ############################################################################################# DASHBOARD

# @app.route( "/dashboard", methods = ['GET'] )
# def privateWall():
#     if 'users_id' not in session:
#         return redirect('/logout')
#     data = {
#         'users_id': session['users_id']
#     }
#     users = User.get_userBy_id(data)
#     user = User.get_all_users(data)
#     result = Car.get_all_cars()
#     return render_template( "dashboard.html", userwall = users, users1 = user, carsDB = result )

# ############################################################################################# ADD RECIPE

# @app.route("/add", methods = ['GET'] )
# def displayAddNewCar():
#     data = {
#         'users_id': session['users_id']
#     }
#     users = User.get_userBy_id(data)
#     return render_template( "addcar.html", userwall = users)


# ################################################################################################### LOG OUT

# @app.route('/logout')
# def userlogout():
#     session.clear()
#     return redirect('/')
