from api.views.hospital_view import PredictDoctorView
from django.urls import path

urlpatterns = [
    path("recommend-doctor/", view=PredictDoctorView.as_view(), name="recommend-doctor"),
]
