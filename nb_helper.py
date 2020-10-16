import pynetbox
import requests
from requests.auth import HTTPBasicAuth
import urllib3
import os
from dotenv import load_dotenv

load_dotenv()

# DISABLE CERT WARNINGS/CHECKS FOR SELF SIGNED CERTS #
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
session = requests.Session()
session.verify = False

# CONNECT TO DEV/PRD NETBOX ENVIROMENT #
nb_dev = pynetbox.api(
    os.getenv("DEV_URL"),
    token=os.getenv("DEV_TOKEN") # TOKEN IS LOADED INTO ENV FROM .env FILE #
)


nb_prd = pynetbox.api(
    os.getenv("PRD_URL"), 
    token=os.getenv("PRD_TOKEN") # TOKEN IS LOADED INTO ENV FROM .env FILE #
)
nb_prd.http_session = session # USED WITH HTTPS #
