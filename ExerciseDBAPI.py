import requests
import urllib.parse

class ExerciseDBAPI:
    def __init__(self):
        self.mainURL = "https://exercisedb.p.rapidapi.com/exercises"
        self.headers = {
            "x-rapidapi-key": "YOUR OWN API KEY",
            "x-rapidapi-host": "exercisedb.p.rapidapi.com"
        }
        self.cache = {}

        self.requestCount = 0

    def fetchAllExercises(self):
        response = requests.get(self.mainURL, headers = self.headers)
        if response.status_code == 200:
            return response.json()
        print("Error fetching all exercises: " + str(response.status_code))
        return []
    
    def fetchBodyPart (self, bodyPart):
        self.requestCount += 1
        print(f"API Request #{self.requestCount}: Fetching exercises for body part '{bodyPart}'")

        if bodyPart in self.cache:
            return self.cache[bodyPart]
        url = self.mainURL + "/bodyPart/" + bodyPart
        response = requests.get(url, headers = self.headers)
        if response.status_code == 200:
            self.cache[bodyPart] = response.json()
            return self.cache[bodyPart]
        print("Error fetching exercises for body part " + bodyPart + ": " + str(response.status_code))
        return []
    
    def fetchBodyPartList(self):
        url = self.mainURL + "/bodyPartList"
        response = requests.get(url, headers = self.headers)
        if response.status_code == 200:
            return response.json()
        print("Error fetching body part list: " + str(response.status_code))
        return []
    
    def fetchEquipment(self, equipment):
        url = self.mainURL + "/equipment/" + equipment
        response = requests.get(url, headers = self.headers)
        if response.status_code == 200:
            return response.json()
        print("Error fetching exercises for equipment " + equipment + ": " + str(response.status_code))
        return []
    
    def fetchRateLimit(self):
        response = requests.get(self.mainURL, headers=self.headers)
        if response.status_code == 200:
            rate_limit = response.headers.get("X-RateLimit-Limit")
            remaining = response.headers.get("X-RateLimit-Remaining")
            reset_time = response.headers.get("X-RateLimit-Reset")
            print("Rate Limit: " + str(rate_limit))
            print("Remaining Requests: " + str(remaining))
            print("Rate Limit Resets At: " + str(reset_time))
            return {
                "Rate Limit": rate_limit,
                "Remaining Requests": remaining,
                "Reset Time": reset_time
            }
        else:
            print("Failed to fetch rate limit. Status Code: " + str(response.status_code))
            return {}




    
exerciseAPI = ExerciseDBAPI()

all_exercises = exerciseAPI.fetchAllExercises()
print("Fetched " + str(len(all_exercises)) + " exercises.")

body_part = "back"
back_exercises = exerciseAPI.fetchBodyPart(body_part)
print("Fetched " + str(len(back_exercises)) + " exercises for body part: " + body_part)

body_parts = exerciseAPI.fetchBodyPartList()
print("Available body parts: " + ", ".join(body_parts))

#equipment = "barbell"
#barbell_exercises = exerciseAPI.fetchEquipment(equipment)
#print("Fetched " + str(len(barbell_exercises)) + " exercises for equipment: " + equipment)