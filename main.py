from typing import Optional
from dotenv import load_dotenv
import requests
import smtplib
import os



load_dotenv()

MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")


class IssNotifier:
    """Creates an OBJ class of ISS notifier"""
    
    def __init__(self, my_lat:float, my_long:float, email:str, password:str):
        self.my_lat = my_lat
        self.my_long = my_long
        self.email = email
        self.password = password



def main() -> None:
     notifier = IssNotifier(my_lat=52.248421, my_long=21.172608,
        email=MY_EMAIL,
        password=PASSWORD 
     )        
        
        
if __name__ =="__main__":
    main()   
        