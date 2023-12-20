from flask import render_template,session,redirect, request,make_response,send_file
import base64
from app import app
from app.models.boxerprofile import BoxerProfile
from app.models.db.profiledatabase import ProfileDatabase
from app.models.imageconverter import ImageConverter

@app.route('/boxer-profile', methods=['GET'])
def boxer_profile():
    
    if not session.get('role') == 'Boxer':
        return redirect('/')

    # get the boxer profile
    profile_db = ProfileDatabase()
    # find boxer with username from current session
    profile = profile_db.find_boxer_profile(session.get('username'))

    return render_template('boxer/boxer-profile.html',profile=profile)

@app.route('/boxer-profile', methods=['POST'])
def update_boxer_profile():

    # get full name 
    fullname = request.form.get("fullname") or "No Name"
    # get weight
    weight = request.form.get("weight") or 0
    # get height
    feet = request.form.get("feet") or 0
    inches = request.form.get("inches") or 0
    # get age
    age = request.form.get("age") or 0
    # get number of fights
    number_of_fights = request.form.get("number_of_fights") or 0
    # get year of experience
    years_of_experience = request.form.get("years_of_experience") or 0 
    # get language
    language = request.form.get("language") or "English"
    # get zip code
    zipcode = request.form.get("zipcode") or 00000
    # get image
    picture = request.files['picture']
    imageconverter = ImageConverter()

    if not picture:
        encoded_pic = request.form.get("picture_base64")
    else:
        encoded_pic = imageconverter.convert_image_to_base64(picture)

    new_boxer_profile = BoxerProfile(
        session.get('username'),
        fullname,
        age,
        weight,
        number_of_fights,
        feet,
        inches,
        language,
        years_of_experience,
        zipcode,
        encoded_pic
    )
    profile_db = ProfileDatabase()
    profile_db.find_and_update_boxer_profile(session.get('username'),new_boxer_profile.to_dict())
    return redirect('/boxer-profile')



