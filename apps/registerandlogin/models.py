from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['fname']) < 2:
            errors["fname"] = "First name should be more than 2 characters"
        if len(postData['lname']) < 2:
            errors["lanme"] = "Last name should be more than 2 characters"
        return errors

class User(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    cpassword = models.CharField(max_length=255)
    objects = UserManager()