
from django.contrib import admin
from django.urls import path, include

from users.views import IndexView, SignUp

urlpatterns = [

    path('signup/', SignUp.as_view(), name='signup'),
]


