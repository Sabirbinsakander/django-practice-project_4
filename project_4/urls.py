from django.contrib import admin
from django.urls import path, include

#from views import contacts
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home),
    path("first_app/", include("first_app.urls")),
    path("contacts/", views.contacts)
]
