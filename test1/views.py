from django.shortcuts import render
from .forms import MyForm
def index(request):
    form=MyForm
    if request.method == "GET":
        print("Hello")
    return render(request,"index.html",{"form":form})