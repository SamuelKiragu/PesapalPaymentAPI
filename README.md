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

4. Make migrations and migrate
```bash
pip makemigrations
pip migrate
```

5. Run server

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
curl --location 'https://cybqa.pesapal.com/pesapalv3/api/Transactions/SubmitOrderRequests'\
--header 'Content-Type: application/json'\
--header 'Authorization: Bearer'\
--data-raw '{
"id": "TEST13434",
"currency": "KES",
"amount": 100.00,
"description": "description"",
"callback_url: "here"
"notification_id": "sdfdasdf"
"billing_address": {
"email_address": "john.doe@example.com",
"first_name": "John"
"last_name": "Doe"
}
}'
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
