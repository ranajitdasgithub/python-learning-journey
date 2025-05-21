from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page_view(request):
    return HttpResponse("Hello, world!")


def about_page_view(request):
    context={
        "name":"John Doe",
        "age": 23
    }
    return render(request,"pages/about.html", context)

def company_page_view(request):
    return render(request,"company.html")  # render the company.html template
