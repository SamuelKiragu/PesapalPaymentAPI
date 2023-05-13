from datetime import datetime, timezone
import pytz
import requests
import json

# consumer_key and consumer_secret
# for testing purposes ONLY
# production key and secret should be separated from code
CONSUMER_KEY = 'qkio1BGGYAXTu2JOfm7XSXNruoZsrqEW'
CONSUMER_SECRET = 'osGQ364R49cXKeOYSpaOnT++rHs='

# important state variables
ACCESS_TOKEN = None
PAYPAL_SERVER_URL = 'https://cybqa.pesapal.com'
TOKEN_EXPIRY = None

def get_access_token(consumer_key, consumer_secret):
    url = f'{PAYPAL_SERVER_URL}/pesapalv3/api/Auth/RequestToken'

    payload = json.dumps({
        'consumer_key': consumer_key,
        'consumer_secret': consumer_secret
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # Make request for access token. 
    # Try until successful. Factors in Network Error
    response = requests.request('POST', url, headers=headers, data=payload)
    response_text = json.loads(response.text)
    while(response_text['status'] != '200'):
        response = requests.request('POST', url, headers=headers, data=payload)
        response_text = json.loads(response.text)
    
    # Return ExpiryDate and Token
    # Status used for testing success
    return {
            'ExpiryDate': datetime.strptime(response_text['expiryDate'][:-2],
                                        '%Y-%m-%dT%H:%M:%S.%f'),
            'Status': 'Success',
            'Token': response_text['token'],
            }

# Function Test
# Function Name: get_access_token
# Expected )Result: 'Success'
assert get_access_token(CONSUMER_KEY, CONSUMER_SECRET)['Status'] == 'Success'

def is_token_expired(token_expiry):
    now_datetime = datetime.now(timezone.utc)
    delta = now_datetime - pytz.utc.localize(token_expiry)
    return True if delta.total_seconds() > 500 else False

# Function Test
# Function Name: is_token_expired
# Expected Result: 'False', token has just been fetched
res = get_access_token(CONSUMER_KEY, CONSUMER_SECRET)
TOKEN =  res['Token']
TOKEN_EXPIRY = res['ExpiryDate']
assert is_token_expired(TOKEN_EXPIRY) == False
