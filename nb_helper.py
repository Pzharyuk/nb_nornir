import pynetbox
import requests
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

session = requests.Session()
session.verify = False

nb_dev = pynetbox.api(
    'http://dev_netbox_url',
    token='token goes here'
)
nb_dev.http_session = session


nb_prd = pynetbox.api(
    'https://prod url goes here', 
    token='token goes here'
)
nb_prd.http_session = session
