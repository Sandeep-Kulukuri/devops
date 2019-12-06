from . import views
from django.urls import path



urlpatterns=[
    path("",views.index),
    path('base', views.base, name='base'),
    path('login', views.login,name='login'),
    path('register', views.register,name='register'),

    path('recess', views.recess,name='recess'),

    path('aboutus', views.aboutus,name='aboutus'),
    path('user', views.user, name='user'),
    path('addquetions', views.addquetions, name='addquetions'),
    path('adddomain', views.adddomain, name='adddomain'),
    path('addsub', views.addsub, name='addsub'),
    path('addcontest', views.addcontest, name='addcontest'),
    path('afteraddq', views.afteraddq, name='afteraddq'),
    path('uploadque', views.uploadque, name='uploadque'),
    path('gotosub/enroll', views.enroll, name='enroll'),
    path('gotosub/onemark', views.questionsshow, name='questionshow'),
    path('gotosub/twomark', views.questionsshow, name='questionshow'),
    path('gotosub/threemark', views.questionsshow, name='questionshow'),
    path('gotosub/marksevaluation', views.marksevaluation, name='marksevaluation'),

    path('viewusers',views.viewusers,name='viewusers'),


]
