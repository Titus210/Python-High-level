import random
import pandas as pd
from datetime import datetime, timedelta

# List of possible pet names
pet_names = ['Buddy', 'Max', 'Fluffy', 'Luna', 'Charlie', 'Rocky', 'Daisy', 'Bailey', 'Lucy', 'Milo',
             'Jack', 'Sadie', 'Toby', 'Bella', 'Cooper', 'Oliver', 'Chloe', 'Gizmo', 'Simba', 'Sophie']


# List of names to choose from
submitter_names = ['Emily', 'Michael', 'Avery', 'Daniel', 'Madison', 'Ethan', 'Mia', 'Alexander', 'Olivia', 'William', 'Isabella', 'James', 'Sophia', 'Benjamin', 'Charlotte', 'Lucas', 'Amelia', 'Mason', 'Evelyn', 'Jacob', 'Harper', 'Noah', 'Abigail', 'Elijah', 'Emily', 'Logan', 'Ava', 'Caleb', 'Mila', 'Matthew', 'Aria', 'Dylan', 'Luna', 'Connor', 'Scarlett', 'Luke', 'Chloe', 'Liam', 'Nora', 'Sebastian', 'Ella', 'Henry', 'Aaliyah', 'Wyatt', 'Gianna', 'Nathan', 'Sofia', 'Isaac', 'Layla', 'Samuel', 'Zoe', 'Owen', 'Victoria', 'Levi', 'Riley', 'Gabriel', 'Ellie', 'Hannah', 'Leah', 'Lillian', 'Audrey', 'Aiden', 'Elizabeth', 'Grayson', 'Grace', 'Eva', 'Penelope', 'Hazel', 'Stella', 'Lily', 'Maya', 'Elliot', 'Nova', 'Aurora', 'Zara', 'Miles', 'Savannah', 'Bryce', 'Willow', 'Jordan', 'Bella', 'Lincoln', 'Skylar', 'Ezra', 'Lila', 'Carter', 'Elliana', 'Nicholas', 'Makayla', 'Evelyn', 'Jasmine', 'Harmony', 'Genevieve', 'Ruby', 'Ada', 'Adeline', 'Violet', 'Naomi']


# List of possible species
species = ['Dog', 'Cat', 'Hedgehog', 'Rabbit', 'Bird', 'Fish', 'Turtle', 'Hamster', 'Guinea Pig', 'Ferret']

# List of possible breeds
dog_breeds = ['Golden Retriever', 'Labrador Retriever', 'Poodle', 'Chihuahua', 'Bulldog', 'Siberian Husky',
              'German Shepherd', 'Boxer', 'Pug', 'Dalmatian']
cat_breeds = ['Siamese', 'Persian', 'Bengal', 'Maine Coon', 'Sphynx', 'Ragdoll', 'British Shorthair',
              'American Shorthair', 'Scottish Fold', 'Russian Blue']
hedgehog_breeds = ['African Pygmy', 'Algerian', 'Four-toed', 'Long-eared', 'Somali']
rabbit_breeds = ['Lionhead', 'Netherland Dwarf', 'Flemish Giant', 'Mini Rex', 'Holland Lop']
bird_breeds = ['Parakeet', 'Cockatiel', 'Canary', 'Budgie', 'Lovebird']
fish_breeds = ['Goldfish', 'Betta', 'Guppy', 'Angelfish', 'Neon Tetra']
turtle_breeds = ['Red-eared Slider', 'Painted Turtle', 'Box Turtle', 'Musk Turtle', 'Diamondback Terrapin']
hamster_breeds = ['Syrian', 'Dwarf', 'Roborovski', 'Chinese', 'Russian']
guinea_pig_breeds = ['American', 'Peruvian', 'Teddy', 'Abyssinian', 'Silkie']
ferret_breeds = ['Albino', 'Black Sable', 'Cinnamon', 'Dark-eyed White', 'Sable']

# List of possible pet descriptions
pet_descriptions = ['Friendly and active', 'Loyal and smart', 'Independent and curious', 'Playful and energetic',
                    'Affectionate and cuddly', 'Shy and reserved', 'Mischievous and fun-loving', 'Brave and fearless',
                    'Sociable and outgoing', 'Quiet and contemplative']

# List of possible submission dates (past year)
dates = []

for i in range(20):
    year = random.choice([2018, 2019, 2022])
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    date = datetime(year=year, month=month, day=day).strftime(
        '%m/%d/%Y %H:%M:%S')
    dates.append(date)

# List of possible vaccinations
vaccinations = ['Canine Parvovirus', 'Canine Distemper', 'Canine Rabies', 'Feline Calicivirus', 'Feline Viral Rhinotracheitis',
                'Feline Panleukopenia', 'Avian Influenza', 'Avian Pox', 'Salmonella', 'Tetanus']

# Generate random pet data
pet_data = []
for i in range(20):
    pet_name = random.choice(pet_names)
    submitter_name = random.choice(submitter_names)
    species_type = random.choice(species)
    if species_type == 'Dog':
        breed = random.choice(dog_breeds)
    elif species_type == 'Cat':
        breed = random.choice(cat_breeds)
    elif species_type == 'Hedgehog':
        breed = random.choice(hedgehog_breeds)
    elif species_type == 'Rabbit':
        breed = random.choice(rabbit_breeds)
    elif species_type == 'Bird':
        breed = random.choice(bird_breeds)
    elif species_type == 'Fish':
        breed = random.choice(fish_breeds)
    elif species_type == 'Turtle':
        breed = random.choice(turtle_breeds)
    elif species_type == 'Hamster':
        breed = random.choice(hamster_breeds)
    elif species_type == 'Guinea Pig':
        breed = random.choice(guinea_pig_breeds)
    elif species_type == 'Ferret':
        breed = random.choice(ferret_breeds)

    pet_description = random.choice(pet_descriptions)
    sex = random.choice(['M', 'F'])
    age = random.randint(0, 14)
    submission_date = random.choice(dates)
    vaccinations_list = random.sample(vaccinations, random.randint(1, 3))
    vaccinations_str = ', '.join(vaccinations_list)

    pet_data.append([pet_name, submitter_name, species_type, breed,
                    pet_description, sex, age, submission_date, vaccinations_str])

# Create a pandas DataFrame from the pet data
pet_df = pd.DataFrame(pet_data, columns=['Pet', 'Submitter', 'Species', 'Breed',
                      'Pet Description', 'Sex', 'Age', 'Submission Date', 'Vaccinations'])

# Save the pet data to an Excel file
pet_df.to_excel('pet_data.xlsx', index=False)
