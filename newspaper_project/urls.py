
from django.contrib import admin
from django.urls import path

from users.views import testView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', testView),
]


