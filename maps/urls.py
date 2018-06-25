from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name="home_page"),
    path('get_dot/<int:dot_id>', views.get_dot, name="get_dot"),
]
