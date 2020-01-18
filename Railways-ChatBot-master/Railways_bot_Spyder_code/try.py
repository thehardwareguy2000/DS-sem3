from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot=ChatBot('Bot')
trainer=ListTrainer(bot)

for files in os.listdir('Training_Data'):
    data=open('C:/Users/leesa\Desktop\Railways-ChatBot-master\Railways_bot_Spyder_code\Training_Data' + files+'r').readlines()
    trainer.train(data)


while True:
    message = input('You:')
    if message.strip() !='Bye':
        reply=bot.get_response(message)
        print('Chatbot:',reply)
    if message.strip()=='Bye':
        print('ChatBot: Bye')
        break
