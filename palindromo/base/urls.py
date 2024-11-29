from django.urls import path

from palindromo.base.views import HomeView

app_name = 'base'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
