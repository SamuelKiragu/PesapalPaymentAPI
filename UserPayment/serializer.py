from rest_framework import serializers

class CustomerSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=10)
    email_address = serializers.EmailField()
    country_code = serializers.CharField(max_length=15)
    first_name = serializers.CharField(max_length=20)
    middle_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    line_1 = serializers.CharField(max_length=20)
    line_2 = serializers.CharField(max_length=20)
    city = serializers.CharField(max_length=20)
    state = serializers.CharField(max_length=20)
    postal_code = serializers.CharField(max_length=20)
    zip_code = serializers.CharField(max_length=20)

class OrderSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=10)
    currency = serializers.CharField(max_length=4)
    amount = serializers.FloatField()
    description = serializers.CharField(max_length=50)
    callback_url = serializers.URLField()
    notification_id = serializers.CharField(max_length=50)
    billing_address = CustomerSerializer()

# Serialization Tests
# CustomerSerializer
class Customer:
    def __init__(self, phone_number, email_address, country_code,
                 first_name, middle_name, last_name, line_1,
                 line_2, city, state, postal_code, zip_code):
        self.phone_number = phone_number
        self.email_address = email_address
        self.country_code = country_code
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.line_1 = line_1
        self.line_2 = line_2
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.zip_code = zip_code

customer = Customer(
            phone_number =  '',
            email_address = 'john.doe@example.com',
            country_code = 'KE',
            first_name = 'John',
            middle_name = '',
            last_name = 'Doe',
            line_1 = '',
            line_2 = '',
            city = '',
            state = '',
            postal_code = '',
            zip_code = '')

serializer = CustomerSerializer(customer)
serializer.data # serialized data

# Serialization Test
# OrderSerialization
class Order:
    def __init__(self, id, currency, amount, description, 
                 callback_url, notification_id, billing_address):
        self.id = id
        self.currency = currency
        self.amount = amount
        self.description = description
        self.callback_url = callback_url
        self.notification_id = notification_id
        self.billing_address = billing_address

order = Order(
        id = 'AA1122-3344ZZ',
        currency = 'KES',
        amount = 100.00,
        description = 'Payment description goes here',
        callback_url = 'https://www.myapplication.com/response-page',
        notification_id = 'sdffssj;fas-adf;sdfjsfd',
        billing_address = customer)
serializer = OrderSerializer(order)
serializer.data # serialized data
