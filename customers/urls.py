from django.urls import path
from . import views
from django.conf.urls import include, url

app_name = 'customers'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # path('check/', views.checkCustomer, name='check'),
    # path('forgotPassword', views.forgotPassword, name='forgotPassword'),
    # path('userInfo', views.userInfo, name='userInfo'),
    # path('listCoach', views.listCoach, name='listCoach'),
    # path('datve', views.datve, name='datve'),
    # path('_login', views.loginView, name='login'),
    #  path('quanlyve', views.quanlyveView, name='login'),

]