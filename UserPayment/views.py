from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from UserPayment import pesapal
from UserPayment.serializers import *
import random

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SubmitOrder(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    PESAPAL_TOKEN = None

    def post(self, request, format=None):
        """
        Validate required data 
        """
        if not (request.data.get("amount") and
                request.data.get("email_address")):
            return Response("Error")
        
        # Create billing address object
        billing_address = pesapal.BillingAddress(
                            email_address = request.data.get("email_address"),
                            first_name = request.data.get("first_name"),
                            last_name = request.data.get("last_name")
                        )

        """
        Pesapal API call
        """
        # Get pesapalToken
        if not self.PESAPAL_TOKEN or pesapal.is_token_expired(PESAPAL_TOKEN):
            self.PESAPAL_TOKEN = pesapal.get_access_token()
        # Submit Order
        results = pesapal.submit_order_request(
            id=random.randint(10000,99999),
            currency='KES',
            amount=request.data['amount'],
            description='Payment',
            callback_url='http://127.0.0.0:8000/',
            ipn_url='http://127.0.0.0:8000/',
            billing_address= BillingAddressSerializer(billing_address).data,
            token=self.PESAPAL_TOKEN["token"]
        )
        return Response(results)
