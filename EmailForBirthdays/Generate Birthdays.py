import csv
import random
from faker import Faker
from datetime import datetime, timedelta

# Generate random data using the Faker library
fake = Faker()

def generate_random_data(num_records):
    with open('aniversariantes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['nome', 'email', 'idade', 'data_de_nascimento'])
        for _ in range(num_records):
            name = fake.name()
            email = fake.email()
            birth_date = fake.date_of_birth(minimum_age=18, maximum_age=90)
            age = (datetime.now().date() - birth_date).days // 365
            writer.writerow([name, email, age, birth_date.strftime('%Y-%m-%d')])

        # Add an additional record for today's birthday
        today = datetime.now().date()
        today_bithday_name = fake.name()
        today_bithday_email = fake.email()
        today_birth_date = today.replace(year=today.year - random.randint(18, 90))
        today_age = (today - today_birth_date).days // 365
        writer.writerow([today_bithday_name, today_bithday_email, today_age, today_birth_date.strftime('%Y-%m-%d')])

# Number of records to generate
num_records = 10

# Generate random data and write to the CSV file
generate_random_data(num_records)

print(f'{num_records + 1} records successfully generated in aniversariantes.csv.')
