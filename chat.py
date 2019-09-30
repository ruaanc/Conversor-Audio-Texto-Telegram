from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot("Meu Bot")

quest = ""
while (quest != "exit"):
    quest = input("Você: ")

    response = bot.get_response(quest)

    print("Bot: ", response)