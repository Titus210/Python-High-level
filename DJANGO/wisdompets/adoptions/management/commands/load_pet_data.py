from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from adoptions.models import Pet, Vaccine
from pytz import UTC

DATE_FORMAT = "%m/%d/%Y %H:%M"

VACCINE_NAMES = [
    "Feline Calicivirus",
    "Feline Viral Rhinotracheitis",
    "Tetanus"
    "Salmonella",
    "Tetanus",
    "Feline Panleukopenia",
    "Avian Influenza",
    "Canine Rabies",
    "Canine Distemper",
    "Avian Pox",
    "Canine Parvovirus"
]

ALREADY_LOADED_ERROR_MESSAGE = """
 If you need to reload the pet data from the CSV file,
 first delete the database db.sqlite3 file to destroy the database.
 Then run `python manage.py migrate` for a new empty
 database with tables"""


class Command(BaseCommand):
     # Show this when the user types help
    help = "Loads data from pet_data.csv into our Pet model"

    def handle(self, *args, **options):
        if Vaccine.objects.exists() or Pet.objects.exists():
            print('Pet data already loaded...exiting.')
            print(ALREADY_LOADED_ERROR_MESSAGE)
            return
        print("Creating vaccine data")
        for vaccine_name in VACCINE_NAMES:
            v = Vaccine(name=vaccine_name)
            v.save()
        print("Loading pet data for pets available for adoption")
        for row in DictReader(open('./pet_data.csv')):
            pet = Pet()
            pet.name = row['Pet']
            pet.submitter = row['Submitter']
            pet.species = row['Species']
            pet.breed = row['Breed']
            pet.description = row['Pet Description']
            pet.sex = row['Sex']
            pet.age = row['Age']
            raw_submission_date = row['Submission Date']
            submission_date = UTC.localize(datetime.strptime(raw_submission_date, DATE_FORMAT))
            pet.submission_date = submission_date
            pet.save()
            
            raw_vaccination_names = row['Vaccinations']
            vaccination_names = [name for name in raw_vaccination_names.split('|') if name]
            for vac_name in vaccination_names:
                v = Vaccine.objects.get(name=vac_name)
                pet.vaccinations.add(v)
            pet.save()
