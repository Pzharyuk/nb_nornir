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

# CONNECT TO DEV NETBOX ENVIROMENT #
nb = pynetbox.api(
    os.getenv("NB_URL"), # NB_URL is loaded from  Environmet Variable
    token=os.getenv("NB_TOKEN") # NB_TOKEN is loaded from  Environmet Variable
)
nb.http_session = session # USED WITH HTTPS #
