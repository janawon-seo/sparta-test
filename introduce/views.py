from django.shortcuts import render

def first_view(request):
    return render(request, 'my_test.html')

# Create your views here.
