##################### Hard Starting Project ######################
import datetime as dt
import os
import random
import csv
import smtplib

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }

birthdays_dict = {}
time = dt.datetime.now()
with open("birthdays.csv", newline='') as file:
    files = csv.reader(file)
    next(files)
    for row in files:
        year = int(row[2])
        month = int(row[3])
        day = int(row[4])
        name = row[0]
        email = row[1]
        birthdays_dict[(month, day)] = (name, email)

p_month = time.month
p_day = time.day
check = (p_month, p_day)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp
replacement = ''
for key, value in birthdays_dict.items():
    if key == check:
        folder_path = "letter_templates"
        letters = os.listdir(folder_path)
        random_file = random.choice(letters)
        file_path = "letter_templates/"+random_file
        with open (file_path, 'r') as text_choice:
            text = text_choice.readlines()
            text_str = ''.join(text)
            replacement = text_str.replace('[NAME]', value[0])


# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
my_email = 'levitest29@gmail.com'
password= 'dyiz rath rebs thgb'

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs='leviscott1988@yahoo.com',
        msg=f"Subject: hello \n\n {replacement}"
    )



