from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Welcome to the Doctor Recommendation System!")

urlpatterns = [
    path("", homepage, name="homepage"),
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]
