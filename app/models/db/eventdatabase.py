from pymongo import MongoClient
import certifi
import json
from bson import json_util
from datetime import datetime
import os
ca = certifi.where()

class EventDatabase:
    def __init__(self):
        self.connection_string = os.environ.get("CONNECTION_STRING")
        self.client = MongoClient(self.connection_string, tlsCAFile=ca)
        self.database = self.client.SparFinder
        self.gym_collection = self.database.gym
        self.event_collection = self.database.event
        self.coach_profile_collection = self.database.coachprofile


    def add_event(self,event):
        
        # add the event to the event_collection
        added_event = self.event_collection.insert_one(event)
        added_event_id = added_event.inserted_id

        # add the event to the coach
        self.coach_profile_collection.update_one({'username':event['coach']},{'$push':{'events':added_event_id}})


        # add the event to the gym
        self.gym_collection.update_one({'name':event['gym']},{'$push':{'events':added_event_id}})

    def get_all_events_from_user(self,username):
        events = self.event_collection.find({'coach':username})
        return json.loads(json_util.dumps(events)) 
    
    def get_all_future_events(self):
        current_time = datetime.now().strftime("%Y-%m-%dT%H:%M")
        query = {"date": {"$gt": current_time}}
        events = self.event_collection.find(query)
        return json.loads(json_util.dumps(events))