from django.db import models


class ClinicLocation(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.name)


class Specialty(models.Model):
    name_of_specialty = models.CharField(max_length=255)

    def __str__(self) -> str:
        return str(self.name_of_specialty)

    class Meta:
        verbose_name = "specialty"
        verbose_name_plural = "specialties"


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.ForeignKey(
        Specialty,
        on_delete=models.CASCADE,
    )
    clinic_location = models.ForeignKey(
        ClinicLocation,
        on_delete=models.SET_NULL,  # Use SET_NULL to prevent strict dependency
        null=True,
        blank=True,
    )
    fees = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.specialty} - {self.clinic_location}"

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
