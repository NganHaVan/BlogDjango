from django.urls import path

from account import views

app_name = "account"
urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('profile/edit',
         views.edit_profile, name="edit_profile")
]
