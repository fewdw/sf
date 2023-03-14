from pymongo import MongoClient
import certifi
import json
from bson import json_util
from dotenv import load_dotenv
import os
ca = certifi.where()

class UserDatabase:
    def __init__(self):
        self.connection_string = os.environ.get("CONNECTION_STRING")
        self.client = MongoClient(self.connection_string, tlsCAFile=ca)
        self.database = self.client.SparFinder
        self.user_collection = self.database.user
        self.boxer_profile_collection = self.database.boxerprofile
        self.coach_profile_collection = self.database.coachprofile

    def signup_new_user(self,user):

        # create the new login
        self.user_collection.insert_one(user)

        # create new default profile for boxer
        if user['role'] == 'Boxer':
            new_profile = {
                "username":user['username'],
                "fullname":"",
                "Weight":0,
                "feet":0,
                "inches":0,
                "Age":0,
                "numberoffights":0,
                "zipcode":0,
                "ratings":[],
                "events":[],
                "language":user['language'],
                "yearsofexperience":0,
                "picture": ""
            }
            self.boxer_profile_collection.insert_one(new_profile)
        
        # create new default profile for coach
        if user['role'] == 'Coach':
            new_profile = {
                "username":user['username'],
                "fullname":' ',
                'gyms':[],
                'language':user['language'],
                'events':[],
                "yearsofexperience":0,
                'picture': " "
            }
            self.coach_profile_collection.insert_one(new_profile)


    # if username exists it will return true, else false
    def does_username_exist(self,username):
        user = self.user_collection.find_one({"username":username})
        return user is not None
    
    def get_user_info_by_username(self,username):
        user = self.user_collection.find_one({"username": username})
        return json.loads(json_util.dumps(user))