from django.shortcuts import render, redirect
# Create your views here.
import whois
def index(request):
    if request.method == "POST":
        ip = request.POST.get("ip")
        answer = whois.whois(ip)
        ##dName = answer.get('domain_name')
        print(answer)
        return render(request,'index2.html',{'data':answer})
    else:
        return render(request,"index.html")

def index_call(request):
    return render(request, "index.html")
