from django.shortcuts import render
from introduce.models import AccessLog

def first_view(request):
    access_log = AccessLog()
    access_log.location = "introduce"
    access_log.save()
    return render(request, 'my_test.html')

# Create your views here.
