import os
from pydoc import text
import this
import telepot
from random import choice
from telepot.loop import MessageLoop


# creating /Authenticatin Bot Obj
bot = telepot.Bot(os.getenv('BOT_TOKEN'))

# function responding to telegram user
def dadSaid_Bot(message):

    # retrieving chat identity
    chat_id = message['chat']['id'] 
    # retrieving text from chat
    command = message['text'] 

    # only 1 true condition
    # capitalizing for case insensitivity
    if command.capitalize() == 'Hello':
        
        # using a context manager to read & automatically close file.
        with open('Dad_Seriously.txt') as f:

            #randomly save lines from txt file
            f_contents = choice(f.readlines())
            #concatenating the joke with emojis & sends to user
            bot.sendMessage(chat_id, f_contents + "\U0001F92D\U0001F923")

    # error handling for false values
    else:
        bot.sendMessage(chat_id, "Wanna hear a Joke lol?\n\nSend me a \"Hello\" message \U0001F602")


# creating session by looping main function
MessageLoop(bot, dadSaid_Bot).run_forever()