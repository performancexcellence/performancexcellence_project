from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wellness(request):
    return render(request, 'wellness/test.html')