from django.shortcuts import render

# Create your views here.
def homepage(request):
    context={'blogposts':[1,2,3]}
    return render(request, 'homepage.html',context=context)