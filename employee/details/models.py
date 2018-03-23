from django.db import models
from django.utils import timezone
from django.conf import settings
import django.utils.datetime_safe
import datetime
# Create your models here.
class Employee(models.Model):

    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    Phone_No = models.CharField(max_length=20)
    Email = models.EmailField(unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
   # models.DateTimeField(default=timezone.now, null=True, blank=True)
    # def save(self, *args, **kwargs):
    #     ''' On save, update timestamps '''
    #     if not self.id:
    #         self.created_on = timezone.now()
    #     self.modified_on = timezone.now()
    #     return super(Employee, self).save(*args, **kwargs)
# class BaseModel(models.Model):
#     created_date = models.DateTimeField(auto_now_add=True)
#     modified_date = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         abstract = True
class EmpAddr(models.Model):
    Employee=models.ForeignKey(Employee, null=True)
    Address1=models.CharField(max_length=100)
    Address2=models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


