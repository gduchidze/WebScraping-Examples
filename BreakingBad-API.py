import requests
import json
from win10toast import ToastNotifier
import sqlite3

chara = input("Enter Character Name: ")

url = "https://api.breakingbadquotes.xyz/v1/quotes/200"
response = requests.get(url)
headers = response.headers
# print("Headers:", headers)
# status_code = response.status_code
# print("Status Code:", status_code)
#
if response.status_code == 200:
    d = response.json()
    for char in d:
        if char['author'].lower() == chara.lower():
            quotes = "".join(char['quote'])
            print("Quotes:", quotes)



            conn = sqlite3.connect('breakingbad.db')
            cursor = conn.cursor()


            cursor.execute('''CREATE TABLE IF NOT EXISTS characters
                                          (author TEXT, quote TEXT)''')
            cursor.execute("INSERT INTO characters VALUES (?, ?)",
                           (chara, quotes))

            conn.commit()
            conn.close()

            toaster = ToastNotifier()
            notification_title = "Character Information"
            notification_message = f"Name: {chara}\nquotes: {quotes}"
            toaster.show_toast(notification_title, notification_message)

            break
    else:
        print("!!!!!!")
else:
    print("!!!!!!")
# json_string = json.dumps(response.text)
# file_path = "liza.json"
# with open(file_path, "w") as json_file:
#     json_file.write(json_string)
# print("JSON file created successfully.")