from django.urls import path
from . import views as v

app_name = 'accounts'
urlpatterns = [
    path('accounts/',v.register,name='register'),
    path('',v.loginpage,name='login'),
    path('logout',v.logoutpage,name='logout')
]