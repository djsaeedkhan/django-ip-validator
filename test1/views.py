from django.shortcuts import render
from .forms import CacheCheck
import re
from django.contrib import messages


def index(request):
    form=CacheCheck
    if request.method == "POST":
        pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
        test = pat.match(request.POST.get("ip",''))
        if test:
            messages.add_message(request, messages.INFO, 'Acceptable ip address')
        else:
            messages.add_message(request, messages.INFO, 'Unacceptable ip address')
    return render(request,"index.html",{"form":form})