# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import models

class UserManager(models.Manager):
    def validate_user(self, postData):
        errors = {}
        # validate first and last name
        if len(postData['name']) < 3:
            errors['name'] = "Your name needs to be 3 or more characters"
        # validate email
        try:
            validate_email(postData['email'])
        except ValidationError:
            errors['email'] = "Your email is not valid"
        else:
            if User.objects.filter(email=postData['email']):
                errors['email'] = "This email already exists"

        # validate password
        if len(postData['password']) < 8:
            errors['password'] = "Please enter a longer password, needs to be 8 or more characters"
        if postData['password'] != postData['confirm_pass']:
            errors['confirm_pass'] = "Passwords must match"
        return errors
            
class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class ReviewManager(models.Manager):
    def validate_review(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title needs to be at least 2 characters"
        if len(postData['body']) < 10:
            errors['body'] = "The body for the review needs to be at least 10 characters long"
        return errors

class Review(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=1000)
    rating = models.IntegerField(default=5)
    user = models.ForeignKey(User, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()