from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from .views import CreateUser
from . import views


urlpatterns=[
  path('', views.index, name='index'),
  path('about/', views.about, name="about"),
  path('signup/', CreateUser.as_view()),
  path('login/', obtain_jwt_token),
]
