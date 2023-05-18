from django.urls import path
from  UserPayment.views import *

urlpatterns = [
        path('api-token-auth/', CustomAuthToken.as_view()),
        path('submit_order/', SubmitOrder.as_view()),
        path('users/', UserList.as_view())
]
