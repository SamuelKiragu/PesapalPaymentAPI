from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from  UserPayment.views import *

urlpatterns = [
        path('api-token-auth/', CustomAuthToken.as_view()),
        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
        path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
        path('submit_order/', SubmitOrder.as_view()),
        path('users/', UserList.as_view())
]
