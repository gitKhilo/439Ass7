from rest_framework import serializers
from api.models.hospital import Doctor, Specialty, ClinicLocation


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ["name_of_specialty"]


class ClinicLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicLocation
        fields = ["name", "address"]


class DoctorSerializer(serializers.ModelSerializer):
    specialty = SpecialtySerializer()
    clinic_location = ClinicLocationSerializer()

    class Meta:
        model = Doctor
        fields = [
            "name",
            "specialty",
            "clinic_location",
            "fees",
            "phone",
            "email",
            "rating",
        ]
