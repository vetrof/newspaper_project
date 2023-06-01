
from django.contrib import admin
from django.urls import path, include

from users.views import IndexView, SignUp

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]


