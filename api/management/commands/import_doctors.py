import csv
from django.core.management.base import BaseCommand
from api.models.hospital import Doctor, Specialty, ClinicLocation


class Command(BaseCommand):
    help = "Import doctors from a CSV file"

    def handle(self, *args, **kwargs):
        file_path = "C:\\Users\\hkhal\\Desktop\\Doctor-recommendation-system-main\\Doctor-recommendation-system-main\\HospitalManagement\\doctors_contact_list.csv"

        try:
            with open(file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    specialty, _ = Specialty.objects.get_or_create(
                        name_of_specialty=row['Specialization']
                    )

                    clinic_location, _ = ClinicLocation.objects.get_or_create(
                        name=row['Clinic Location']
                    )

                    Doctor.objects.create(
                        name=row['Doctor Name'],
                        specialty=specialty,
                        clinic_location=clinic_location,
                        fees=row['Fees'],
                        phone=row['Phone'],
                        email=row['Email'],
                        rating=row['Rating'],
                    )
                self.stdout.write(self.style.SUCCESS("Successfully imported doctors"))
        except Exception as e:
            self.stderr.write(f"Error: {e}")
