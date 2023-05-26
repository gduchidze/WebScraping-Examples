import requests
import json
from win10toast import ToastNotifier
import sqlite3

character = input("შეიყვანე პერსონაჟის სახელი: ")

url = "https://hp-api.onrender.com/api/characters"
response = requests.get(url)
# headers = response.headers
# print("Headers:", headers)
# status_code = response.status_code
# print("Status Code:", status_code)
#
if response.status_code == 200:
    data = response.json()
    for char in data:
        if char['name'].lower() == character.lower():
            alternate_names = ", ".join(char['alternate_names'])
            house = char['house']
            gender = char['gender']
            year_of_birth = char['yearOfBirth']

            print("Alternate Names:", alternate_names)
            print("House:", house)
            print("Gender:", gender)
            print("Year of Birth:", year_of_birth)

            conn = sqlite3.connect('character.db')
            cursor = conn.cursor()


            cursor.execute('''CREATE TABLE IF NOT EXISTS characters
                                          (name TEXT, alternate_names TEXT, house TEXT, gender TEXT, year_of_birth INT)''')
            cursor.execute("INSERT INTO characters VALUES (?, ?, ?, ?, ?)",
                           (character, alternate_names, house, gender, year_of_birth))

            conn.commit()
            conn.close()

            toaster = ToastNotifier()
            notification_title = "Character Information"
            notification_message = f"Name: {character}\nHouse: {house}\nGender: {gender}\nYear of Birth: {year_of_birth}"
            toaster.show_toast(notification_title, notification_message)

            break
    else:
        print("პერსონაჟი არ მოიძებნა")
else:
    print("რაღაც შეცდომაა!!!")
# json_string = json.dumps(response.text)
# file_path = "output10.json"
# with open(file_path, "w") as json_file:
#     json_file.write(json_string)
# print("JSON file created successfully.")