from django.shortcuts import render
from introduce.models import AccessLog

#case1
def first_view(request):
    access_log = AccessLog()
    access_log.location = "introduce"
    access_log.save()
    return render(request, 'my_test.html')



    #case2
    #AccessLog.objects.create(
    #    location="introduce"
    #)
# Create your views here.
