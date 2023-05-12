from datetime import datetime
import http.client
import json

# Track the state of token
# This will inform when to get another access token
ACCESS_TOKEN = None
TOKEN_EXPIRY_DATE = None
NOTIFICATION_ID = None

def get_access_token(consumer_key, consumer_secret):
    conn = http.client.HTTPSConnection('cybqa.pesapal.com')
    payload = json.dumps({
        'consumer_key': consumer_key,
        'consumer_secret': consumer_secret
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    conn.request('POST', '/pesapalv3/api/Auth/RequestToken', payload, headers)
    res = conn.getresponse()
    data = res.read()
    res_dict = json.loads(data.decode('utf-8'))

    ACCESS_TOKEN = res_dict['token']
    # TODO: TOKEN_EXPIRY_DATE
    # TOKEN_EXPIRY_DATE = datetime.strptime(res_dict['expiryDate'], '%Y-%m-%dT%I:%M:%S.%fZ')

def register_IPN_URL(url, notification_type):
    return ""

def make_payment(first_name, last_name, 
                 phone_number, email):
    return ""

