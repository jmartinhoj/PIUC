from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('login/', LoginView.as_view(template_name= "accounts/login.html"), name='login'),
    path('register/', views.register, name='register'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout,name='profile'),
    path('feed/', include('feed.urls'))
]
