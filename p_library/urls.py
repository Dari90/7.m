from django.urls import path
from .views import FriendList
 
app_name = 'p_library'
 
urlpatterns = [
    path('friends', FriendList.as_view(), name='friend_form'),
]