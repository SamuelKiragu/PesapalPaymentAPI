from django.urls import path
from  UserPayment import views

urlpatterns = [
        path('users/', views.UserList.as_view())
]
