<<<<<<< HEAD
import requests
import dotenv

# 

def main():

    
    


if __name__ == "__main__":
    main()
=======
import json

import requests
from requests import Response, auth, request
from dotenv import load_dotenv
import os

LOGIN_URL = "https://wellfitness.perfectgym.pl/ClientPortal2/Auth/Login"
CLASSES_URL = "https://wellfitness.perfectgym.pl/ClientPortal2/Classes/ClassCalendar/WeeklyClasses"
MAIN_URL = (
    "https://wellfitness.perfectgym.pl/ClientPortal2/Clubs/Clubs/GetMembersInClubs"
)

load_dotenv("config.env")

LOGIN = os.environ.get("Login", None)
PASS = os.environ.get("Password", None)


def login():
    data = {"RememberMe": "true", "Login": LOGIN, "Password": PASS}
    print(LOGIN, PASS)
    response = s.post(url=LOGIN_URL, json=data)


def get_club_data():
    response = s.post(url=MAIN_URL)
    print(response.json())


def main():
    global s
    s = requests.session()
    login()
    print(s.cookies)
    get_club_data()


if __name__ == "__main__":
    main()
>>>>>>> 225c1e9 (some progress, the login sturcture, requests.session implementation and the main gym data implementation is done)
