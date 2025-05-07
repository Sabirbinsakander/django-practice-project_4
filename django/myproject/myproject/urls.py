from django.contrib import admin
from django.urls import path, include
# from views import contact
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path("myapp/", include("myapp.urls")),
    path('contact/', views.contact)
]
