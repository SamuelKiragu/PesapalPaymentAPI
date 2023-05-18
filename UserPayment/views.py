from django.contrib.auth.models import User
from rest_framework import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

class CreateUser(APIView):
    """
    View to create user
    User is created using
    1. username
    2. password
    3. email
    4. first_name
    5. last_name
    """
    
    def post(self, request, format=None):
        """
        Create new user
        """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
