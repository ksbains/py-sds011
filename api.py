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
    print("the user route is: " + addUserRoute)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    payload = {"username": "bob", "password": "bobISbob", "userType": "GOAT", "homeType": "mansion", "isSmoker":True, "hasAC":True, "houseAge":420420 }
    bob = requests.post(addUserRoute, data=json.dumps(payload), headers=headers)

def addSensor():
    print("Adding the Sensor data now.")

def main():
    print("I will retrieve Alice")
    getOneUser("alice")
    print("I will add the GOAT, bob")
    addUser()
    print("I will now get all of the users")
    getAllUsers()
    print()

main()