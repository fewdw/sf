from flask import jsonify, render_template,session,redirect, request, flash, get_flashed_messages
from app import app
from app.models.gym import Gym
from app.models.db.gymdatabase import GymDatabase
from app.models.imageconverter import ImageConverter

@app.route('/my-gyms')
def my_gyms():

    if not session.get('role') == "Coach":
        return redirect('/')
    
    gymdatabase = GymDatabase()
    gyms = gymdatabase.find_gyms_from_user(session.get('username'))

    message = get_flashed_messages()
    return render_template('coach/my-gyms.html', message=message, gyms=gyms)

@app.route('/my-gyms', methods=['POST'])
def add_gym():

    if not session.get('role') == "Coach":
        return redirect('/')

    # get the information
    name = request.form.get('name')
    phone = request.form.get('phone')
    address = request.form.get('address')
    language = request.form.get('language')
    description = request.form.get('rules')
    picture = request.files['picture']

    # validate form is filled
    if name is None or phone is None or address is None or language is None or description is None or picture is None:
        flash('Gym was not added, please fill form properly')
        return redirect('/my-gyms')
    
    imageconverter = ImageConverter()
    encoded_pic = imageconverter.convert_image_to_base_64(picture)

    # create gym object
    gym = Gym(session.get('username'),name,phone,address,language,description,encoded_pic)
    gym_database = GymDatabase()

    # add it to the database
    if not gym_database.add_new_gym(gym.to_dict()):
        flash('There was an error creating your gym, you can only manage a maximum of 3 gyms.')
        return redirect('/my-gyms')        

    # redirect to gym
    return redirect('/my-gyms')

@app.route('/delete-gym',methods=['POST'])
def delete_gym():

    if not session.get('role') == "Coach":
        return redirect('/')
    
    name = request.form.get('name')
    username = session.get('username')
    
    gym_database = GymDatabase()
    gym_database.delete_gym(username,name)

    return redirect('/my-gyms')


@app.route('/api/gym/rules/<name>', methods=['GET'])
def get_gym_rules_by_name(name):
    gym_database = GymDatabase()
    rules = gym_database.get_gym_rules_by_name(name)
    return jsonify(rules)