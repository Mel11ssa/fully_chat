from django.urls import path

from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('test/', views.testEndPoint, name='test'),
    path('', views.getRoutes),
    #chat
    path('my-messages/<user_id>/', views.MyInbox.as_view()), 
    path('get-message/<sender_id>/<reciever_id>/', views.GetMessages.as_view()),
    path('send-message/', views.SendMessage.as_view()), 
    path('profile/<int:pk>/', views.ProfileDetails.as_view()), 
    path('search/<username>/', views.SearchUser.as_view()),
]
    