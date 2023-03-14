from flask import render_template,session, request
from app import app

@app.route('/about-contact',methods=['GET'])
def about():
    return render_template('about-contact/about-contact.html',role=session.get('role'))

@app.route('/email', methods=['POST'])
def contact():
    pass