from django.shortcuts import render,redirect
from django.contrib import messages

# Create your views here.
def index_content(request):
    return render(request,"index.html")

def form_content(request):
    if request.method == 'POST':
        confirm_message = {"submitted": "Your Application has been submitted Successfully"}
        return render(request,'index.html',confirm_message)
    return render(request,"form.html")