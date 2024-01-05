from django.urls import path
from .views import *

urlpatterns = [
    path('main', main),
    path('home', lambda a:a),
    path('contact', lambda a:a),

]