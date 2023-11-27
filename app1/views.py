from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request,'first.html')

def first2(request):
    return render(request,'first2.html')


