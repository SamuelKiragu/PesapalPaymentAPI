from rest_framework import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

class SubmitOrder(APIView):
    """
    View to submit order
    Makes API call to Pesapal
    Returns a JSON object containing the iframe URL
    """
    
    def post(self, request, format=None):
        # TODO: Response skeleton
        # TODO: Extract Data from request
        # TODO: Add additional data
        # TODO: Make API call to pesapal
        # TODO: Format response
        # TODO: return response

