import requests
from utils.api_endpoint import BaseUrl

auth_token = None
user_name = None
user_id = None
user_email = None

def set_user_info(name, id, email):
    global user_name, user_id, user_email
    user_name = name
    user_id = id
    user_email = email

def set_auth_token(token):
    global auth_token
    auth_token = token

def get_headers(is_auth=True):
    headers = {
        "Content-Type": "application/json"
    }
    if is_auth and auth_token:
        headers["Authorization"] = f"Bearer {auth_token}"
    return headers

def post_request(endpoint, data, is_auth=True):
    url = f"{BaseUrl.BASE_URL}{endpoint}"
    headers = get_headers(is_auth)
    response = requests.post(url, headers=headers, json=data)
    return response.json()

def get_request(endpoint, is_auth=True):
    url = f"{BaseUrl.BASE_URL}{endpoint}"
    headers = get_headers(is_auth)
    response = requests.get(url, headers=headers)
    return response.json()

