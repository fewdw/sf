from pymongo import MongoClient
import certifi
import json
from bson import json_util
from dotenv import load_dotenv
import os
ca = certifi.where()

class ProfileDatabase:
    def __init__(self):
        self.connection_string = os.environ.get("CONNECTION_STRING")
        self.client = MongoClient(self.connection_string, tlsCAFile=ca)
        self.database = self.client.SparFinder
        self.boxer_profile_collection = self.database.boxerprofile
        self.coach_profile_collection = self.database.coachprofile

    # if username exists it will return true, else false
    def find_boxer_profile(self,username):
        user = self.boxer_profile_collection.find_one({"username":username})
        return json.loads(json_util.dumps(user))
    
    def find_coach_profile(self,username):
        user = self.coach_profile_collection.find_one({"username":username})
        return json.loads(json_util.dumps(user))
    
    # update boxer profile
    def find_and_update_boxer_profile(self,username,profile):
        query = {"username":username}

        updated_profile = {
            "$set": profile
        }

        self.boxer_profile_collection.find_one_and_update(query,updated_profile)

    def find_and_update_coach_profile(self,username,profile):
        query = {"username":username}

        updated_profile = {
            "$set":profile
        }

        self.coach_profile_collection.find_one_and_update(query,updated_profile)