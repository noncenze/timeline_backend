from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from .views import CreateUser
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserView, 'user')
router.register(r'extendedusers', views.ExtendedUserView, 'extendeduser')
router.register(r'displaytypes', views.DisplayTypeView, 'displaytype')
router.register(r'timelines', views.TimelineView, 'timeline')
router.register(r'categories', views.CategoryView, 'category')
router.register(r'entries', views.EntryView, 'entry')

urlpatterns=[
  path('', views.index, name='index'),
  path('signup/', CreateUser.as_view()),
  path('login/', obtain_jwt_token),
  path('api/', include(router.urls)),
]