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
            billing_address= UserSerializer(request.user).data,
            token=self.PESAPAL_TOKEN["token"]
        )
        return Response(results)
