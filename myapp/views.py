from django.shortcuts import render, redirect
# Create your views here.
import whois
def index(request):
    if request.method == "POST":
        ip = request.POST.get("ip")
        answer = whois.whois(ip)
        dName = answer.get('domain_name')
        print(dName)
        return render(request,"index.html",{'data':dName})
    else:
        return render(request,"index.html")

