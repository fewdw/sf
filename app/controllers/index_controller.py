from flask import render_template,session
from app import app

@app.route('/', methods=['GET'])
def index():
    return render_template('main_page/index.html',role=session.get('role'))