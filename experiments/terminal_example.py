# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import logging


# Uncomment the following line to enable verbose logging
# logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot("Terminal",
    storage_adapter="chatterbot.storage.JsonFileStorageAdapter",
    # logic_adapters=[
    #     "chatterbot.logic.MathematicalEvaluation",
    #     "chatterbot.logic.TimeLogicAdapter",
    #     "chatterbot.logic.BestMatch"
    # ],
    # input_adapter="chatterbot.input.TerminalAdapter",
    # output_adapter="chatterbot.output.TerminalAdapter",
    database="./database.json"
)

print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        answer = input("Я: ")
        # We pass None to this method because the parameter
        # is not used by the TerminalAdapter
        bot_input = bot.get_response(answer)
        print("Р: {}".format(bot_input))

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break