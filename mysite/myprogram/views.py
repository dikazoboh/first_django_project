from django.http import JsonResponse
from django.shortcuts import render

# Create a function.

def myprogram(request):
    #dictionary
    data ={
        "Name" : "David Ikaz",
        "Track": "Backend(Python)",
        "Message": "Hi Instructor, please do revisions of your assignments."
    }
    #response
    #--return render(request, 'myprogram', {})
    return JsonResponse(data)
