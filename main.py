import json
import requests
from dotenv import load_dotenv
import os
import csv
import re
from datetime import datetime

LOGIN_URL = "https://wellfitness.perfectgym.pl/ClientPortal2/Auth/Login"
CLASSES_URL = "https://wellfitness.perfectgym.pl/ClientPortal2/Classes/ClassCalendar/WeeklyClasses"
CLUB_URL = (
    "https://wellfitness.perfectgym.pl/ClientPortal2/Clubs/Clubs/GetMembersInClubs"
)

load_dotenv("config.env")



LOGIN = os.environ.get("Login", None)
PASS = os.environ.get("Password", None)
GYM = os.environ.get("Gyms", "1")
CSV = bool(os.environ.get("CSV", True))
DISCORD = bool(os.environ.get("Discord", True))


def login(s: requests.sessions.Session):
    data = {"RememberMe": "true", "Login": LOGIN, "Password": PASS}
    print(LOGIN, PASS)
    response = s.post(url=LOGIN_URL, json=data)


def get_club_data(s: requests.sessions.Session, GYMS: list[str]):
    response = s.post(url=CLUB_URL)
    data = response.json()
    valid_data = {}
    for i in data["UsersInClubList"]:
        if i["ClubName"] in GYMS:
            valid_data[i["ClubName"]] = i["UsersCountCurrentlyInClub"]
        
    return valid_data
    
# def get_class_data():
#     response = s.get(url=CLASSES_URL, json={"clubId": 17})
#     print(json.dumps(response.json(), indent=2))

def get_gyms():
    GYMS = re.findall(r"\d+", GYM)
    GYMS_normal = {}
    with open("data/clubs.csv", newline="", encoding="utf-8") as file:
        lines = csv.DictReader(file)
        for i in lines:
            if i["ID"] in GYMS: 
                GYMS_normal[i["ID"]] = i["club_name"]
    
    if len(GYMS) != len(GYMS_normal):
        missing = [i for i in GYMS if i not in GYMS_normal.keys()]
        print(f"Did not match following IDs with clubs.csv: \n{", ".join(missing)}")
    
    return list(GYMS_normal.values())
    
def save_to_CSV(data: dict[str, str]):
    fieldnames = ["GymName", "Date", "Raw ppl count"]
    mode = "r+"
    date = datetime.now().isoformat(timespec="minutes")
    
    if not os.path.exists("data/logs.csv"):
        mode = "a+"
            
    with open("data/logs.csv", mode=mode, newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        if next(csv.reader(file), None) != writer.fieldnames:
            writer.writeheader()
        
        for k,v in data.items():
            writer.writerow({"GymName": k, "Date": date, "Raw ppl count": v})

    
    

def main():
    s = requests.session()
    login(s)
    GYMS = get_gyms()
    data = get_club_data(s, GYMS) 
    if CSV:
        save_to_CSV(data)    
    if DISCORD:
        # discord_webhook()
        ...
    


if __name__ == "__main__":
    main()
