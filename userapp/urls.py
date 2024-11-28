from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns=[

   path("login/", auth_views.loginView.as_views(
       template_name = "user/login.html"
   ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='user/login.html'
    ), name='logout'),
]