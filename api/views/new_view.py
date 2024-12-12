from api.serializers.doctor_serializer import DoctorSerializer
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.models.hospital import Doctor
from django.db.models import Q

class PredictDoctorAPI(APIView):
    class InputSerializer(serializers.Serializer):
        specialty = serializers.CharField(required=False)
        clinic_location = serializers.CharField(required=False)
        max_fees = serializers.DecimalField(
            max_digits=10, decimal_places=2, required=False
        )
        min_rating = serializers.DecimalField(
            max_digits=3, decimal_places=2, required=False
        )

    def post(self, request, *args, **kwargs):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        filters = serializer.validated_data

        # Build the query
        query = Q()
        if "specialty" in filters:
            query &= Q(specialty__name_of_specialty__icontains=filters["specialty"])
        if "clinic_location" in filters:
            query &= Q(clinic_location__name__icontains=filters["clinic_location"])
        if "max_fees" in filters:
            query &= Q(fees__lte=filters["max_fees"])
        if "min_rating" in filters:
            query &= Q(rating__gte=filters["min_rating"])

        # Query the database
        doctors = Doctor.objects.filter(query)

        # Serialize and return the results
        serializer = DoctorSerializer(doctors, many=True)
        return Response(data={"results": serializer.data}, status=status.HTTP_200_OK)
