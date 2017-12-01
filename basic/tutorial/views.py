from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
# Create your views here.

def beginpage(request):
    context = {}
    return render(request, "index.html", context)

def loginpage(request):
    return render(request, "login.html", {})

def contact(request):
    return render(request, "contact.html", {})

def about(request):
    return render(request, "about.html", {})

def profile(request):
    return render(request, "profile.html", {})

def register(request):
    return render(request, "register.html", {})

class Profile(View):
    def get(self, request, *args, **kwargs):
        context = {"user_id" : 1}
        return render(request, "profile.html", context)

#    def post(self, request, *args, **kwargs):
#        context = {"user_id" : }
#        return render(request, "profile.html", context)
#    def put(self, request, *args, **kwargs):
#        context = {"user_id" : kwargs}
#        return render(request, "profile.html", context)

class ProfileTemplateView(TemplateView):
    template_name = 'profile.html'