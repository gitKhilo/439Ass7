import csv
from django.core.management.base import BaseCommand
from api.models.hospital import Doctor, Specialty, ClinicLocation
import os

class Command(BaseCommand):
    help = "Import doctors from doctors_contact_list.csv"

    def handle(self, *args, **kwargs):
        # Set the path to the CSV file
        csv_file_path = os.path.join(
            os.path.dirname(__file__), "doctors_contact_list.csv"
        )

        # Ensure the file exists
        if not os.path.exists(csv_file_path):
            self.stderr.write(f"File not found: {csv_file_path}")
            return

        # Read and import data
        with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Create or get the Specialty
                specialty, _ = Specialty.objects.get_or_create(
                    name_of_specialty=row["Specialization"]
                )

                # Create or get the Clinic Location
                clinic, _ = ClinicLocation.objects.get_or_create(
                    name=row["Clinic Location"],
                    address=row["Clinic Location"],  # Assuming the name is also the address
                )

                # Create the Doctor
                Doctor.objects.create(
                    name=row["Doctor Name"],
                    specialty=specialty,
                    clinic_location=clinic,
                    fees=row["Fees"],
                    phone=row["Phone"],
                    email=row["Email"],
                    rating=row["Rating"],
                )

            self.stdout.write(self.style.SUCCESS("Doctors imported successfully!"))
