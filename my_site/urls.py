"""my_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from p_library import views
from django.conf import settings
from django.conf.urls.static import static
from allauth.account.views import login, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('', views.index),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrement/', views.book_decrement),
    path('redaction_list/', views.redaction_list),
    path('friend_list/', views.friend_list),
    path('library/', views.library),
    path('p/', include('p_library.urls', namespace='p_library')),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', views.user_profil,  name='user_profil'),
    path('index/login/', login, name='login'),  
    path('accounts/profile/logout/', logout, name='logout'),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
