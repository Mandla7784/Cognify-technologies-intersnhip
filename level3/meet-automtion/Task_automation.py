"""
    In this project we create a program that will automate the process of joing metting with google meet
    we use google cloud perhaps for the project database services
"""

import os
import json


from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport import requests



# authorization 

def authorize()-> Credentials:
    client_secrete_file = "./client_secret.json"
    credentials = None

    if os.path.exists("tokes.json"):
        credentials = Credentials.from_authorized_user_file("token.json")


    if credentials is None:
        flow = InstalledAppFlow.from_client_secrets_file(
             client_secrete_file,
             scopes=[
                 "https://www.googleapis.com/auth/meetings.space.created"
             ]
        )




def main():
    ...

if __name__=="__main__":
    main()