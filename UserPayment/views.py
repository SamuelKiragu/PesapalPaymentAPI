from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from UserPayment import pesapal
from UserPayment.serializers import *

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class SubmitOrder(APIView):
    authentication_classes = [TokenAuthentication]
    PESAPAL_TOKEN = None

    def get(self, request, format=None):
        """
        Pesapal API call
        """
        # Throw error if no token specified
        if str(request.user) == 'AnonymousUser':
            content = {'Invalid Token'}
            return Response(content, status.HTTP_403_FORBIDDEN)
        # Get pesapalToken
        if not self.PESAPAL_TOKEN or pesapal.is_token_expired(PESAPAL_TOKEN):
            self.PESAPAL_TOKEN = pesapal.get_access_token()
        # Submit Order
            pesapal.submit_order_request(
                id=#TODO,
                currency='KES',
                amount=request.query_params.get('amount'),
                description='Payment',
                callback_url=#TODO
                ipn_url=#TODO,
                billing_address=#TODO,
                token=self.PESAPAL_TOKEN["token"]
            )
        return Response(self.PESAPAL_TOKEN)
