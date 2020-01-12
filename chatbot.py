from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#import os 
import time 
import asyncio
from telethon import TelegramClient,events

chatbot = ChatBot('Test')

conversation = open('chats.txt', 'r').readlines()

trainer = ListTrainer(chatbot)

trainer.train(conversation)

api_id = 1083717
api_hash = '054ba24e752a247b41a78a9b51ded451'


def main(): 
    # Create the client and connect
    client = TelegramClient('telehandler_session', api_id, api_hash)
    client.start()
    
    @client.on(events.NewMessage(incoming=True))
    async def handler(event):
        request = str(event.raw_text)
        print(request)
        #print(time.asctime(), '-', event.message)
        response = str(chatbot.get_response(request))
        time.sleep(2)
        await event.reply(response)
    
    
    print(time.asctime(), '-', 'Waiting for incoming messages...')
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')
    
    
if __name__ == '__main__':
    main()



#while True:
#    request = input('You: ')
#    response = chatbot.get_response(request)

#    print('Bot: ', response)
