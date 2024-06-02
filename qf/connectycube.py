import requests
import hashlib
import hmac
import time
import random
from datetime import datetime


# Datos de configuración
BASE_URL = 'https://api.connectycube.com'
APP_ID = '7678'
AUTH_KEY = '7Jz5LusMpV2Ugb2'
AUTH_SECRET = 'uZVVgk3kAVmMraV'

#crear signature, es clave para la comunicaciom de la api
def create_signature(params):
    sorted_params = "&".join(f"{key}={value}" for key, value in sorted(params.items()))
    signature = hmac.new(AUTH_SECRET.encode(), sorted_params.encode(), hashlib.sha1).hexdigest()
    return signature
# Función para crear una sesión (Sin un usuario)
def create_session(login = None, password = None):
    url = f'{BASE_URL}/session'
    nonce = str(random.randint(1, 1000000000))
    timestamp = str(int(time.time()))

    params = {
        "application_id": APP_ID,
        "auth_key": AUTH_KEY,
        "nonce": nonce,
        "timestamp": timestamp,
    }

    if login and password:
        params.update({
            "user[login]": login,
            "user[password]": password,
        })

    signature = create_signature(params)
    payload = {
        'application_id': APP_ID,
        'auth_key': AUTH_KEY,
        'nonce': nonce,
        'timestamp': timestamp,
        'signature': signature
    }

    if login and password:
        payload['user'] = {
            'login': login,
            'password': password
        }

    response = requests.post(url, json=payload)
    json_response = response.json()
    if response.status_code == 201:
        token = json_response['session']['token']
        return token
    else:
        raise Exception(f"Error creating session: {response.json()}")

def register_user_connecticube(token, username, email, password):
    url = f'{BASE_URL}/users'
    user_data = {
        'user': {
            'login': username,
            'email': email,
            'password': password,

        }
    }
    print(token)
    headers = {
        'CB-Token': token,
        'Content-Type': 'application/json',
    }
    response = requests.post(url, json=user_data, headers=headers)
    #debugin
    print (response)
    return response.json()

def create_dialog(token, occupants_ids):
    typeDidalog = 2
    url = f'{BASE_URL}/chat/Dialog'
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

    body = {
        'type': typeDidalog,
        'occupants_ids': occupants_ids,
        'name': f"CHAT: {timestamp}"
    }

    headers = {
        'CB-Token': token,
        'Content-Type': 'application/json',
    }

    print(body)
    response = requests.post(url, json=body, headers=headers)
    print(response)
    return response.json()
#login hace referencia al username
def search_user(token, login):
    url = f'{BASE_URL}/users/v2'
    params = {
        'login': login
    }
    headers = {
        'CB-Token': token,
        'Content-Type': 'application/json',
    }

    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error retrieving user: {response.json()}")