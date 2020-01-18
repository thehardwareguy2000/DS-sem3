import pyttsx3  
import speech_recognition  as sr 
import webbrowser as wb 
from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer
import os

# there is a file named db create when u run this code which may cretae bot to give unwanted response so to remove it we use this code
if os.path.exists("db.sqlite3"):
    os.remove("db.sqlite3")

# Ask user that did he want to interact verbally or y typing
interact = input("""How you want to interact with Bot i.e via voice or via typing your Query
Type 'V' or 'v' for voice interaction and 'T' or 't' for Typing interaction \n""")
    
# code to train bot with general FAQ's of railways   
# code to train bot with general FAQ's of railways   
kang = ChatBot('yml')
conv = open('Training_Data/Greeting_FAQ.yml','r').readlines()
trainer=ListTrainer(kang)
trainer.train(conv)
conv = open('Training_Data/Train_running_status_FAQ.yml','r').readlines()
trainer=ListTrainer(kang)
trainer.train(conv)
conv = open('Training_Data/Train_platform_enquery_FAQ.yml','r').readlines()
trainer=ListTrainer(kang)
trainer.train(conv)
conv = open('Training_Data/Seat_availability_FAQ.yml','r').readlines()
trainer=ListTrainer(kang)
trainer.train(conv)
conv = open('Training_Data/Train_time_table_FAQ.yml','r').readlines()
trainer=ListTrainer(kang)
trainer.train(conv)
conv = open('Training_Data/Trains_between_stations_FAQ.yml','r').readlines()
trainer=ListTrainer(kang)
trainer.train(conv)
conv = open('Training_Data/Stations_FAQ.yml','r').readlines()
trainer=ListTrainer(kang)
trainer.train(conv)
conv = open('Training_Data/Station_connected_FAQ.yml','r').readlines()
trainer=ListTrainer(kang)
trainer.train(conv)
conv = open('Training_Data/Fare_enquiry_FAQ.yml','r').readlines()
trainer=ListTrainer(kang)
trainer.train(conv)
conv = open('Training_Data/Platform_locator_FAQ.yml','r').readlines()
trainer=ListTrainer(kang)
trainer.train(conv)
conv = open('Training_Data/Coach_layout_FAQ.yml','r').readlines()
trainer=ListTrainer(kang)
trainer.train(conv)
conv = open('Training_Data/PNR_FAQ.yml','r').readlines()

trainer=ListTrainer(kang)
trainer.train(conv)





# Code if user want to interact verbally and want to change gender of his bot assitent 
if interact == 'V' or interact == 'v':
    speaker = pyttsx3.init()
    speaker.say("Would you like a male, or a female virtual assistant to assist you ? ")
    speaker.runAndWait()
    mic  =  sr.Microphone()
    r = sr.Recognizer()
    while(1):
        with mic as source:
            print("say :")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)

        if "female" in text.lower() or "women" in text.lower() or "girl" in text.lower():
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice',voices[1].id)
            rate=engine.getProperty('rate')
            engine.setProperty('rate',135)
            speaker.say("Feamle Assistent, Activated")
            speaker.runAndWait()
            break


        elif "man" in text.lower()  or "male" in text.lower() or "mail" in text.lower() or "boy" in text.lower():
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice',voices[0].id)
            rate=engine.getProperty('rate')
            engine.setProperty('rate',135)
            speaker.say("Male Assistent, Activated")
            speaker.runAndWait()
            break


        else: 
            speaker = pyttsx3.init()
            speaker.say("You were not clear enough to convey. Please try again.")
            speaker.runAndWait()
            print("You were not clear enough to convey. Please try again.")
            
############################################################################
# code for part if user want to interact verbally with bot
if interact == 'V' or interact == 'v':
    mic  =  sr.Microphone()
    r = sr.Recognizer()
    speaker = pyttsx3.init()
    speaker.say("Hi I am K The virtual Assistent, How may i help you.")
    speaker.runAndWait()
    while True:
        mic  =  sr.Microphone()
        r = sr.Recognizer()
        with mic as source:
            print("say :")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)
            messege = text
            
        if "book ticket" in messege.strip() or 'book some tickets' in  messege.strip() or "ticket book" in messege.strip() or "railway ticket" in messege.strip() or "train ticket" in messege.strip() or "book train" in messege.strip():
            print('I know u want to book Train Tickets So i am redirecting u to IRCTC Website')
            speaker = pyttsx3.init()
            speaker.say("I know u want to book Train Tickets So i am redirecting u to I R C T C Website")
            speaker.runAndWait()
            wb.open_new_tab('http://www.irctc.co.in/nget/train-search')
            break

        elif 'bye' in messege.strip():
            print('KANG: bye bye, have a nice day')
            speaker = pyttsx3.init()
            speaker.say("bye bye, have a nice day.")
            speaker.runAndWait()
            break

        else:
            response = kang.get_response(messege)
            print('KANG: ', response)
            speaker = pyttsx3.init()
            speaker.say(response)
            speaker.runAndWait()
            
# Code for the part if user want to interact by typing his query           
else:
    print("Hi I am K The virtual Assistent, How may i help you.")
    while True:
        mic  =  sr.Microphone()
        r = sr.Recognizer()
        with mic as source:
            messege = input("You: ")

        if "book ticket" in messege.strip() or 'book some tickets' in  messege.strip() or "ticket book" in messege.strip() or "railway ticket" in messege.strip() or "train ticket" in messege.strip() or "book train" in messege.strip():
            print('I know u want to book Train Tickets So i am redirecting u to IRCTC Website')
            wb.open_new_tab('http://www.irctc.co.in/nget/train-search')
            break

        elif 'bye' in messege.strip():
            print('KANG: bye bye, have a nice day')
            speaker = pyttsx3.init()
            speaker.say("bye bye, have a nice day.")
            speaker.runAndWait()
            break

        else:
            response = kang.get_response(messege)
            print('KANG: ', response)



