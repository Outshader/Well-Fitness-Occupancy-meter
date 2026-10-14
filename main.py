import json
import requests
import requests
from dotenv import load_dotenv
import os

LOGIN_URL = "https://wellfitness.perfectgym.pl/ClientPortal2/Auth/Login"
CLASSES_URL = "https://wellfitness.perfectgym.pl/ClientPortal2/Classes/ClassCalendar/WeeklyClasses"
CLUB_URL = (
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
    response = s.post(url=CLUB_URL)
    global data 
    data = response.json()
    
def get_class_data():
    response = s.get(url=CLASSES_URL, json={"clubId": 17})
    print(json.dumps(response.json(), indent=2))

def main():
    global s
    s = requests.session()
    login()
    get_club_data()
    get_class_data()


if __name__ == "__main__":
    main()
