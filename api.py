# In this file, will connect to the BreatheEaZy API to send the sensor data out. 
import json
import requests
import pprint
import simplejson
API = "https://breatheazy-api.herokuapp.com/"
MGR = 'https://breatheazy-api.herokuapp.com/mongo/'
piRoute = API + "pi/"


def getAllUsers(): 
    allUsersRoute = MGR + 'allUsers'
    users = requests.get(allUsersRoute)
    pprint.pprint(users.json())


def getOneUser(username):
    oneUserRoute = MGR + username
    user = requests.get(oneUserRoute)
    pprint.pprint(user.json())


def addUser():
    addUserRoute = MGR + 'user'
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    payload = {"username": "bob", "password": "bobISbob", "userType": "GOAT", "homeType": "mansion", "isSmoker":True, "hasAC":True, "houseAge":420420 }
    bob = requests.post(addUserRoute, data=json.dumps(payload), headers=headers)


def addSensor(pm2_5):
    addSensorRoute = MGR + 'sensor'
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    payload = {
        "pm2_5Data": [{
            "pm2_5": pm2_5,
            "dateTime": "2021-04-20 -4:20:00"
        }]
    }
    sensorData = requests.post(addSensorRoute, data=json.dumps(payload), headers = headers)
    pprint.pprint(sensorData.json())

def getOneSensor():
    # still need to do
    print("darn")


def main():
    # print("I will retrieve Alice")
    # getOneUser("alice")
    # print("I will add the GOAT, bob")
    # addUser()
    print("I will now get all of the users")
    getAllUsers()
    print()
    addSensor("25")






main()