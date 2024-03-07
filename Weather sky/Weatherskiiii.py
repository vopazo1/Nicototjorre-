
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

import base64
from email.message import EmailMessage

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]
import datetime

import requests
from datetime import date, timedelta, datetime


message_content = []
import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

#List with 0 and 1 as one cordinaat -> then put in the for loop. Make a dictionary
lalo = {"LesTroisVallees":["45.3499986", "6.5999976"],
        "Sölden": ["46.96667", "11.0"],
        "Chamonix-Mont Blan":["45.92375", "6.86933"],
         "Val di Fass":["462600", "114200"],
        "Salzburger Sportwelt":["473203", "134099"],
        "Alpenarena Flims-Laax-Faler":["468070", "92664"],
        "Kitzsteinhorn Kapru":["471973", "126936"],
        "Ski Arlber":["472102", "102179"],
        "Espace Kill":["454227", "69270"],
        "Spindleruv Mlyn":["507271", "156063"]
}

message_content = []

choose = input('Choose an option:\n ')

email = input("Your e-mail:")
print(email)

snow = []



fstring = f"https://api.openweathermap.org/data/2.5/forecast?lat={lalo.get("LesTroisVallees")[0]}&lon={lalo.get("LesTroisVallees")[1]}&appid=ed379326780c2209ece8e4d227451e35&units=metric"


 #= f'https://api.openweathermap.org/data/2.5/forecast?lat={}&lon={}&appid=ed379326780c2209ece8e4d227451e35&units=metric'

#Location_1 = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=45.3499986&lon=6.5999976&appid=ed379326780c2209ece8e4d227451e35&units=metric")
#Location_2 = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=46.96667&lon=11.0&appid=ed379326780c2209ece8e4d227451e35&units=metric")
#Location_3 = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=45.92375&lon=6.86933&appid=ed379326780c2209ece8e4d227451e35&units=metric")
#Location_4 = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=462600&lon=114200&appid=ed379326780c2209ece8e4d227451e35&units=metric")
#Location_5 = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=473203&lon=134099&appid=ed379326780c2209ece8e4d227451e35&units=metric")
#Location_6 = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=468070&lon=92664&appid=ed379326780c2209ece8e4d227451e35&units=metric")
#Location_7 = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=471973&lon=126936&appid=ed379326780c2209ece8e4d227451e35&units=metric")
#Location_8 = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=472102&lon=102179&appid=ed379326780c2209ece8e4d227451e35&units=metric")
#Location_9 = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=454227&lon=69270&appid=ed379326780c2209ece8e4d227451e35&units=metric")
#Location_10 = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=507271&lon=156063&appid=ed379326780c2209ece8e4d227451e35&units=metric")


#for lalo in


