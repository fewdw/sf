from pymongo import MongoClient
import certifi
import json
from bson import json_util
import os
from dotenv import load_dotenv

load_dotenv()
ca = certifi.where()

class GymDatabase:
    def __init__(self):
        self.connection_string = os.environ.get("CONNECTION_STRING")
        self.client = MongoClient(self.connection_string, tlsCAFile=ca)
        self.database = self.client.SparFinder
        self.gym_collection = self.database.gym
        self.coach_profile_collection = self.database.coachprofile

    def find_gyms_from_user(self, username):
        gyms = self.gym_collection.find({"username": username})
        return json.loads(json_util.dumps(gyms))
    
    def find_gym_names_from_user(self,username):
        gyms = self.coach_profile_collection.find({"username": username}, {"gyms": 1, "_id": 0})
        return json.loads(json_util.dumps(gyms[0]['gyms']))

    def add_new_gym(self,gym):
        # if gym name already exists, dont create it
        if self.gym_collection.find_one({"name":gym['name']}) is not None:
            return False
        
        coach = self.coach_profile_collection.find_one({"username": gym['username']})
        if len(coach["gyms"]) == 2:
            return False

        # create gym
        self.gym_collection.insert_one(gym)

        # add gym to coach
        self.coach_profile_collection.update_one(
            {'username': gym['username']}, 
            {'$push':{'gyms':gym['name']}}
        )
        return True
    
    def delete_gym(self,username, name):
        # delete gym
        self.gym_collection.delete_one({"name": name})

        # remove name from coach gym list
        query = {"username": username}

        coach = self.coach_profile_collection.find_one(query)

        updated_gyms = coach["gyms"]
        updated_gyms.remove(name)
        print(updated_gyms)
        update_query = {"$set": {"gyms": updated_gyms}}
        self.coach_profile_collection.update_one(query, update_query)


    def get_gym_rules_by_name(self,name):
        gym = self.gym_collection.find_one({"name":name})
        return gym['description'] or "This gym currently has no rules"
    

    def get_gym_language_by_name(self,name):
        gym = self.gym_collection.find_one({"name":name})
        return str(gym['language'])


    def get_gym_picture_by_name(self,name):
        gym = self.gym_collection.find_one({"name":name})
        return str(gym['picture'])
    
    def get_gym_address_by_name(self,name):
        gym = self.gym_collection.find_one({"name":name})
        return str(gym['address'])
        