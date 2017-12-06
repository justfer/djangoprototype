from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Account
#account functionalities here.

def DisplayAccounts(request):
    template_name = 'accounts/accounts.html'
    queryset = Account.objects.all()
    context = { "object_list" : queryset}
    return render(request, template_name, context)