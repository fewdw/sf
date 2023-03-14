from app import app
from flask import render_template, request, redirect, session, flash, get_flashed_messages
from app.models.user import User
from app.models.db.userdatabase import UserDatabase
from flask_session import Session
import bcrypt

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# LOGIN ROUTES
@app.route('/login', methods = ['GET'])
def login_page():

    if session.get('username') is not None:
        return redirect('/')
    message = get_flashed_messages()
    return render_template('/login_signup/login.html',message=message)

@app.route('/login', methods = ['POST'])
def login_page_verify():
    
    if session.get('username') is not None:
        return redirect('/')
    
    username = request.form.get('username')
    password = request.form.get('password')

    # check if form is none
    if username is None or password is None:
        flash('username and password are required')
        return redirect('/login')

    # declare userdatabase object
    user_db = UserDatabase()

    # if username does not exist
    if not user_db.does_username_exist(username):
        flash('username does not exist')
        return redirect('/login')
    
    # get user information by username
    user = user_db.get_user_info_by_username(username)
    
    # check if password is correct
    if not bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
        flash('wrong password')
        return redirect('/login')
    
    # create session
    session['username'] = user['username']
    session['language'] = user['language']
    session['role'] = user['role']

    # redirect home page
    return redirect('/')
    

# SIGNUP ROUTES
@app.route('/signup',methods = ['GET'])
def signup_page():
    
    if session.get('username') is not None:
        return redirect('/')
    
    message = get_flashed_messages()
    return render_template('/login_signup/signup.html', message=message)

@app.route('/signup',methods = ['POST'])
def signup_page_verify():

    if session.get('username') is not None:
        return redirect('/')

    # declare userdatabase object
    user_db = UserDatabase()

    # get information from the form
    username = request.form.get('username')
    password = request.form.get('password')
    role = request.form.get('role')
    language = request.form.get('language')

    # check if form is none
    if username is None or password is None or role is None or language is None:
        flash('please fill all fields of the form properly')
        return redirect('/signup')

    # make sure role is boxer or coach
    if role not in ['Boxer','Coach']:
        flash('User has to be Boxer or Coach')
        return redirect('/signup')
    
    # make sure language is french or english
    if language not in ['English','French']:
        flash('Language has to be English or French')
        return redirect('/signup')
    
    # make sure username is not taken
    if user_db.does_username_exist(username):
        flash('Username already exists')
        return redirect('/signup')

    # hash password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode()

    # create new user model
    new_user = User(username,hashed_password,role,language)

    # add new user to the DB
    user_db.signup_new_user(new_user.to_dict())
    
    # create session and redirect to main page
    session['username'] = username
    session['language'] = language
    session['role'] = role

    return redirect('/')


# sign out route
@app.route('/signout')
def signout():
    session['username'] = None
    session['language'] = None
    session['role'] = None
    return redirect('/')