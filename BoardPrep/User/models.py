from django.db import models

from Subscription.models import Subscription


# Create your models here.


class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    user_name = models.CharField(null=False, max_length=255, blank=False)
    password = models.CharField(null=False, max_length=255, blank=False)
    email = models.CharField(null=False, max_length=255, blank=False)
    registration_date = models.DateField()
    last_login = models.DateField()


class Student(User):
    specialization = models.CharField(null=False, max_length=255, blank=False)
    institution = models.CharField(null=False, max_length=255, blank=False)
    subscription = Subscription()


class Tutor(User):
    specialization = models.CharField(null=False, max_length=255, blank=False)
    years_of_teaching = models.IntegerField(default=0, null=False)
    rating = models.FloatField(default=0, null=False)


class Teacher(User):
    name = models.CharField(null=False, max_length=255, blank=False)
    specialization = models.CharField(null=False, max_length=255, blank=False)
    institution_id = models.ForeignKey('Institution.Institution', on_delete=models.SET_NULL, blank=True, null=True, related_name='institutionID')