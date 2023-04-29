# Imports
import os
from dotenv import load_dotenv
import discord
import discordclient

# Constants
load_dotenv()
TOKEN = os.getenv('TOKEN')

# Discord connection
intents = discord.Intents.all()
client = discordclient.BotClient(intents=intents)
client.run(TOKEN)
