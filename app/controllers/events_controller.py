from flask import render_template,session,redirect, request, flash, get_flashed_messages
from app import app
from app.models.datetimechecker import DateTimeChecker
from app.models.db.eventdatabase import EventDatabase
from app.models.db.gymdatabase import GymDatabase
from app.models.event import Event

@app.route('/my-events')
def my_events():
    
    if session.get('role') == "Boxer":
        return render_template("boxer/my-events.html",role = session.get('role')) 
    if session.get('role') == "Coach":
        # get all gyms for a user, retrieve name only
        gymdatabase = GymDatabase()
        gyms = gymdatabase.find_gym_names_from_user(session.get('username'))
        messages = get_flashed_messages()

        # create two lists, one for future events, one for past events
        future_events = []
        past_events = []

        # get all events from user
        eventdatabase = EventDatabase()
        events = eventdatabase.get_all_events_from_user(session.get('username'))
        
        # classify list of events
        datetimechecker = DateTimeChecker()

        for event in events:
            if datetimechecker.is_date_later_than_current_time(event['date']):
                future_events.append(event)
            else:
                past_events.append(event)

        return render_template("coach/my-events.html",role = session.get('role'),messages = messages, gyms=gyms, future_events = future_events, past_events = past_events)
    return redirect('/')
    
    
@app.route('/add-new-event', methods=['POST'])
def add_event():

    # validate session
    if not session.get('role') == "Coach":
        return redirect('/')
    
    # get gym, date and rules
    gym = request.form.get('gym')
    date = request.form.get('date')
    rules = request.form.get('rules')
    max_attendees = int(request.form.get('max_attendees'))

    # validate
    if max_attendees is None or max_attendees < 2 or max_attendees > 15:
        flash("Please select a valid number of attendees for this event.")
        return redirect('/my-events')

    # validate
    if gym is None:
        flash("Failed to add a an event, please select a gym.")
        return redirect('/my-events')
    
    datetimechecker = DateTimeChecker()
    if not datetimechecker.is_date_later_than_current_time(date):
        flash("Please select a later time for the event.")
        return redirect('/my-events')
    
    readable_date = datetimechecker.date_to_readable_format(date)
    
    # get gym language and image
    gymdatabase = GymDatabase()

    gym_language = gymdatabase.get_gym_language_by_name(str(gym))
    gym_picture = gymdatabase.get_gym_picture_by_name(str(gym))
    gym_address = gymdatabase.get_gym_address_by_name(str(gym))

    # create model
    event = Event(
        session.get('username'),
        gym,
        gym_address,
        date,
        readable_date,
        gym_language,
        rules,
        gym_picture,
        max_attendees
    )

    # add the event to db
    eventdatabase = EventDatabase()
    eventdatabase.add_event(event.to_dict())
    

    # redirect to events
    return redirect('/my-events')