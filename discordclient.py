# Imports
import sqlite3
import discord
import databaseutil

# Fetch Training Data
database = sqlite3.connect("fartass2.db")
cursor = database.cursor()


# Bot Client
class BotClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        query = databaseutil.getMessages()
        print(f'Message from {message.author}: {message.content}')
