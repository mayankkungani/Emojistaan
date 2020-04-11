from django.db import models
from django.contrib.auth.models import User	


# Create your models here.
class chatemojiss(models.Model):
    #created=models.DateTimeField(auto_now=False, auto_now_add=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.CharField(max_length=50)
    def __unicode__(self):
        return self.message
    
    def __str__(self):
        return self.message
    

class chatmsgs(models.Model):
    #created=models.DateTimeField(auto_now=False, auto_now_add=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.CharField(max_length=50)
    def __unicode__(self):
        return self.message

    def __str__(self):
        return self.message

