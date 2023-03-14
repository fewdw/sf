from flask import render_template,session,redirect, request
from app import app
import base64
from app.models.coachprofile import CoachProfile
from app.models.db.profiledatabase import ProfileDatabase
from app.models.imageconverter import ImageConverter

@app.route('/coach-profile', methods=['GET'])
def coach_profile():
    if not session.get('role') == 'Coach':
        return redirect('/')

    # get the boxer profile
    profile_db = ProfileDatabase()
    # find boxer with username from current session
    profile = profile_db.find_coach_profile(session.get('username'))

    return render_template('coach/coach-profile.html',profile=profile)

@app.route('/coach-profile', methods=['POST'])
def update_coach_profile():

    fullname = request.form.get("fullname") or "No Name"
    years_of_experience = request.form.get("years_of_experience") or 0
    language = request.form.get("language") or "English"

    picture = request.files['picture']
    imageconverter = ImageConverter()

    if not picture:
        encoded_pic = request.form.get("picture_base64")
    else:
        encoded_pic = imageconverter.convert_image_to_base_64(picture)
    
    new_boxer_profile = CoachProfile(
        session.get('username'),
        fullname,
        language,
        years_of_experience,
        encoded_pic
    )
    profile_db = ProfileDatabase()
    profile_db.find_and_update_coach_profile(session.get('username'),new_boxer_profile.to_dict())
    return redirect('/coach-profile')
    
    