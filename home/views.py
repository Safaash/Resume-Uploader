from django.shortcuts import render,redirect
from .models import Resume
from .forms import ResumeForm
from django.contrib import messages
# Create your views here.
def home(request):
    fm=ResumeForm()
    return render(request,'home.html',{'fm':fm})
def submit(request):
    if request.method=='POST':
        fm=ResumeForm(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
            messages.success(request,"Resume Uploaded Sucessfully!!! ")
    return redirect('/')
def list(request):
    resume=Resume.objects.all()
    return render(request,'list.html',{'resume':resume})
# candidates lists
def details(request,id):
    resume=Resume.objects.get(pk=id)
    return render(request,'details.html',{'resume':resume})