from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .form import *

# Create your views here.

def tes(request):
    if request.method=="POST":
        form = BukuTamuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tes")
       
    context ={}

    # add the dictionary during initialization
    context["dataset"] = Berita.objects.all()
    context["data"] = BukuTamu.objects.all()
    return render(request, "tes.html", context)
