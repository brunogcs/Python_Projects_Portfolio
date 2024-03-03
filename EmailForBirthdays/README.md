# Generating Birthday Data and Sending Birthday Emails

This is a small Python script that generates random birthday data and writes it to a CSV file named `aniversariantes.csv`. It utilizes the `Faker` library to create fictional names, email addresses, birthdates, and ages.

After completing the initial part, the script proceeds to read the previously generated CSV file containing birthday information and sends birthday messages via email using the SMTP server (MailHog).


## How It Works

1. The script creates a CSV file named birthdays.csv.
2. It writes a header line with the fields: name, email, age, and birth_date.
3. Next, it generates random data for the specified number of records (in this example, 10 records).
4. For each record:
    - Generates a random name.
    - Generates a random email address.
    - Calculates the age based on the randomly generated birthdate.
    - Writes this data to the CSV file.
5. Finally, it adds an additional record for today’s birthday, intended for future use in the send_birthday_emails function:
    - Generates a random name and email address, setting the birth date to today.
    - Calculates the age based on the randomly generated birthdate, ensuring it is a valid birthday.
    - Writes this data to the CSV file.
6. The script reads the CSV file and checks if the birthdate matches the current date.
7. If there are birthdays on the day, it sends a birthday message to each individual.
