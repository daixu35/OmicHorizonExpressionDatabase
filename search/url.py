from django.urls import path, include, re_path

from search import views

urlpatterns = [
    re_path("^search/$", views.seach_home, name="search_home"),
    re_path("^update/$", views.update, name="update"),
    re_path("^contact/$", views.contact, name="contact"),
    re_path("^contactSuccess/$", views.contactSuccess, name="contactSuccess"),
    re_path("^FAQ/$", views.FAQ, name="FAQ"),
    re_path("^result/.*$", views.result, name="result"),
]