# Pesapal Payment API
This is an implementation of pesapal APIs. It allows for the creation of a user account, getting an access token using the user account, and finally making payment via pesapal.

## Getting Started

### Prerequisites

1. Python
2. Pip

```bash
python --version
# Printed to stdout
# Python 3.10.9

pip --version
# Printed to stdout
# Pip 23.1.2
```

### Installing

1. Clone repository

```bash
git clone https://github.com/SamuelKiragu/PesapalPaymentAPI.git
```

2. Create virtual environment and activate

```bash
python -m venv /env
source env/bin/activate
```

3. Install required python packages

```bash
pip install django django-rest python-dotenv requests pytz
```
4. Create .env file in the root of the project directory and add the following settings

```bash
DEBUG= # True or False
# Pesapal settings vary depending on whether you are using for testing or production purposes
PESAPAL_CONSUMER_KEY= # URL to acess pesapal consumer key
PESAPAL_CONSUMER_SECRET= # URL to access pesapal consumer secret
PESAPAL_SERVER_URL= # URL to access pesapal API
SECRET_KEY= # Secret key to be used by django
```

5. Make migrations and migrate
```bash
pip makemigrations
pip migrate
```

6. Run server

```
python manage.py runserver
```

## Usage
1. Create a customer account. Details needed are username, first_name, last_name, email_address, and password
```bash
curl --location 'http://127.0.0.1:8000/users/' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
"username": "JoeDoe",
"first_name": "Joe",
"last_name": "Doe",
"email": "joedoe@example.com",
"password": "1234"
}'
```
3. Get Access Token using username and password
```bash
curl --location 'http://127.0.0.1:8000/api-token-auth/' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
"username": "JoeDoe",
"password": "1234"
}'
```
4. Use Access Token to submit an order
```bash
curl --location 'http://127.0.0.1:8000/submit_order/?amount=1000' \ 
--header 'Accept: application/json' \ 
--header 'Authorization: Token {token_from_step_2}'
```

## API Endpoints



## Built With

* [Django](https://djangoproject.com/) - Python Web Framework
* [Django REST](https://django-rest-framework.org) - Toolkit for building web APIs
* [Pesapal API 3.0](https://developer.pesapal.com/) - Pesapal is a payment platform in Africa

## Authors

* **Samuel Kiragu** - [SamuelKiragu](https://github.com/SamuelKiragu)

## License

None

## Acknowledgments
* [PurpleBooth](https://github.com/PurpleBooth) - Provided README template
