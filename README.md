# Pesapal Payment API


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
2. Get Access Token using username and password
3. Use Access Token to submit an order

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
