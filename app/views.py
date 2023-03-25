from django.shortcuts import render

# Create your views here.
def bootstrap_cdn(request):
    return render(request,'bootstrap_cdn.html')
def rcb(request):
    return render(request,'rcb.html')
