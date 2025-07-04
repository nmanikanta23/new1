from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
   if request.method=='POST':
      a=int(request.POST.get('num1'))
      b=int(request.POST.get('num2'))
      c=request.POST.get('op')
      if c=='add':
         result=a+b

      #return render(request,'home.html',{'result':result})
      return redirect('result',result)
      
   return render(request,'home.html',{'name':'purple'})

def result(request,result):
   
   return render(request,'result.html',{'result':result})
   
   

