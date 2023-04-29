# Imports
import sqlite3
import discord
import chat
import databaseutil

# Fetch training data
database = sqlite3.connect("fartass2.db")
cursor = database.cursor()

# Initialize chatbot
bot = chat.FartassChatbot()
query = databaseutil.getMessages()

# Train chatbot
bot.corpusTrainer.train("chatterbot.corpus.english")
bot.listTrainer.train(query)


# Bot Client
class BotClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if self.user.mentioned_in(message):
            await message.reply(content=bot.chatbot.get_response(message.clean_content))
            return

        databaseutil.addMessage(message.clean_content)
        bot.listTrainer.train([message.clean_content])
        print(f'Message from {message.author}: {message.clean_content}')
