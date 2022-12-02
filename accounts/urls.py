from django.urls import path
from .views import RegisterBuyerView, LogoutBuyerView, LoginBuyerView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterBuyerView.as_view(), name='register'),
    path('logout/', LogoutBuyerView.as_view(), name='logout'),
    path('login/', LoginBuyerView.as_view(), name='login'),
]
