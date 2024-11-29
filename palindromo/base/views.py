from django.shortcuts import render
from django.views import View

# Create your views here.


class HomeView(View):
    """
    Simple Home page, to show that it's working.
    """

    def get(self, request, *args, **kwargs):
        return render(request, 'base/home.html')
