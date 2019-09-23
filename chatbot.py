from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot("Meu Bot")

convI = ("Oi", "Olá", "Tudo bem ?", "Sim e com você? ","Estou bem" "Que ótimo")

convA = ("Que animes você gosta ?", "Naruto, Shingeki no kyojin, nanatsu no taizai")

convB = ("Que time você torce ?", "Santa Cruz", "Gosta da seleção brasileira? ", "Sim", "Gosta do Neymar ?", "Não, só cai", "Não")

convC =("O que você faz da vida ?", "Sou apenas um bot", "Gosta de conversar com as pessoas ?", "Depende...", "Você é legal", " Você Também")

trainer = ListTrainer(bot)

trainer.train(convI)
trainer.train(convA)
trainer.train(convB)
trainer.train(convC)

quest = ""
while (quest != "exit"):
    quest = input("Você: ")

    response = bot.get_response(quest)

    print("Bot: ", response)
