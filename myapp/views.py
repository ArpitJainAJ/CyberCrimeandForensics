from django.shortcuts import render, redirect
# Create your views here.

def index(request):
    if request.method == "POST":
        ip = request.POST.get("ip")
        print(ip)
        return render(request,"index.html")
    else:
        return render(request,"index.html")

