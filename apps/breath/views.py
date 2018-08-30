# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import *

# Create your views here.

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.filter(email=email)
    if len(user) > 0:
        is_pass = bcrypt.checkpw(password.encode(), user[0].password.encode())
        if is_pass:
            request.session['id'] = user[0].id
            messages.success(request, 'Logged In!')
            return redirect('/reviews')
        else:
            messages.error(request, "Incorrect email and/or password")
            return redirect('/login-page')
    else:
        messages.error(request, "User does not exist")
    return redirect('/login-page')

def register(request):
    errors = User.objects.validate_user(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/register-page')
    else:
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        User.objects.create(name=name, email=email, password=hashed_pw)
        messages.success(request, 'User Registered')
        return redirect('/login-page')

def index(request):
    return render(request, 'breath/index.html')

def about(request):
    return render(request, 'breath/about.html')

def register_page(request):
    return render(request, 'breath/register.html')

def login_page(request):
    return render(request, 'breath/login.html')

def gallery(request):
    return render(request, 'breath/gallery.html')

def map(request):
    return render(request, 'breath/map.html')

def reviews(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews
    }
    return render(request, 'breath/reviews.html', context)

def add_review(request):
    errors = Review.objects.validate_review(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)
        return redirect('/reviews')
    else:
        user = User.objects.get(id=request.session['id'])
        title = request.POST['title']
        body = request.POST['body']
        rating = request.POST['rating']
        Review.objects.create(title=title, body=body, rating=rating, user=user)
        messages.success(request, 'Review Created')
        return redirect('/reviews')

def contact(request):
    return render(request, 'breath/contact.html')

