from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("thanos", views.thanos, name="thanos"),
    path("david", views.david, name="david")

]