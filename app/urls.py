from app.views import index, register_client
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('register/', register_client, name='register_client'),

]
