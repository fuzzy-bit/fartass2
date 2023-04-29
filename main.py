# Imports
import os
from dotenv import load_dotenv
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
import sqlite3
import discord
import discordclient
import databaseutil

# Constants
load_dotenv()
TOKEN = os.getenv('TOKEN')

# Discord connection
intents = discord.Intents.all()
client = discordclient.BotClient(intents=intents)

# Initialize chatbot
chatbot = ChatBot("Queggle Aron")
corpusTrainer = ChatterBotCorpusTrainer(chatbot)
listTrainer = ListTrainer(chatbot)
query = databaseutil.getMessages()

# Train
corpusTrainer.train("chatterbot.corpus.english")
listTrainer.train(query)

# print(chatbot.get_response("Hello, how are you today?"))
client.run(TOKEN)
