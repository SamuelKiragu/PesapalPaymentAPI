from datetime import datetime, timezone
import pytz
import requests
import json

# Important variables
# for testing purposes ONLY
# production key and secret should be separated from code

# Testing get_access_token()
CONSUMER_KEY = 'qkio1BGGYAXTu2JOfm7XSXNruoZsrqEW'
CONSUMER_SECRET = 'osGQ364R49cXKeOYSpaOnT++rHs='
# Testing register_IPN_URL()
IPN_URL = 'https://www.myapplication.com/ipn'
# Testing submit_order_request()
CALLBACK_URL = 'https://www.myapplication.com/response-page'
BILLING_ADDRESS = {
        'email_address': 'john.doe@example.com',
        'phone_number': None,
        'country_code': '',
        'first_name': 'John',
        'middle_name': '',
        'last_name': 'Doe',
        'line_1': '',
        'line_2': '',
        'city': '',
        'state': '',
        'postal_code': None,
        'zip_code': None
}
# Used in multiple tests.
# Will be assigned values after running some functions
TOKEN = None
TOKEN_EXPIRY = None
NOTIFICATION_ID = None

# Paypal server url
PAYPAL_SERVER_URL = 'https://cybqa.pesapal.com'

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



def register_IPN_URL(url, token):
    url = f'{PAYPAL_SERVER_URL}/pesapalv3/api/URLSetup/RegisterIPN'

    payload = json.dumps({
        'url': url,
        'ipn_notification_type': 'GET'
    })
    headers = {
            'Accept': 'application/json',
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
    }

    response = requests.request('POST', url, headers=headers, data=payload)
    return json.loads(response.text)


# Function Test
# Function Name: register_IPN_URL
# Expected Result: dictionary d['status'] == '200'
assert register_IPN_URL(IPN_URL, TOKEN)['status'] == '200'
res = register_IPN_URL(IPN_URL, TOKEN)
NOTIFICATION_ID = res['ipn_id']



def submit_order_request(id, currency, amount, description,
                         callback_url, notification_id,
                         billing_address, token):
    url = f'{PAYPAL_SERVER_URL}/pesapalv3/api/Transactions/SubmitOrderRequest'

    payload = json.dumps({
        'id': id,
        'currency': currency,
        'amount': amount,
        'description': description,
        'callback_url': callback_url,
        'notification_id': notification_id,
        'billing_address': billing_address
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    response = requests.request('POST', url, headers=headers, data=payload)
    return json.loads(response.text)


# Function Test
# Function Name: submit_order_request
# Expected Results: dictionary d where d['status'] == '200'
assert submit_order_request(
        id = '1233235',
        currency = 'KES', 
        amount = 100,
        description = 'Payment description goes here',
        callback_url = CALLBACK_URL,
        notification_id = NOTIFICATION_ID,
        billing_address = BILLING_ADDRESS,
        token = TOKEN
        )['status'] == '200'
