from django.contrib import admin

from .models.hospital import Doctor, ClinicLocation, Specialty

# Register your models below

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "specialty",
        "clinic_location",
        "fees",
        "phone",
        "email",
        "rating",
    )
    list_filter = (
        "specialty",
        "clinic_location",
        "rating",
    )


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = (
        "name_of_specialty",
    )
    list_filter = (
        "name_of_specialty",
    )


@admin.register(ClinicLocation)
class ClinicLocationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "address",
    )
    list_filter = (
        "name",
        "address",
    )
