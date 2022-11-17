from django.urls import path
from .import views

urlpatterns=[
    path('',views.signup,name='signup'),
    path('login',views.user_login,name='login'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profile,name='profile'),
    # path('changepass',views.changepass,name='changepass')

]