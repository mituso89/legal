import os
from django.urls import path, include

app_name = os.getcwd().split(os.sep)[-1]


urlpatterns = (
    path(
        'admin_user/',
        include('legalapi.app.admin_user.urls'),
    )
)