from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^login-page$', views.login_page),
    url(r'^register-page$', views.register_page),
    url(r'^about$', views.about),
    url(r'^gallery$', views.gallery),
    url(r'^map$', views.map),
    url(r'^reviews$', views.reviews),
    url(r'^add_review$', views.add_review),
    url(r'^contact$', views.contact),
]