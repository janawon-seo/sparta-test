from django.db import models

class AccessLog(models.Model):
    created_at = models.DateTimeField("접속 시간", auto_now_add=True, )
    location = models.CharField("접속경로", max_length=50)

        




# Create your models here.
