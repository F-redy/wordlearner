from django.urls import path

from apps.users import views

app_name = 'users'

urlpatterns = [
    path('registration/', views.RegistrationUserView.as_view(), name='registration'),
]
