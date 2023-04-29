# Imports
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer
import databaseutil


# Chatbot
class FartassChatbot:
    def __init__(self):
        self.chatbot = ChatBot("Queggle Aron")
        self.corpusTrainer = ChatterBotCorpusTrainer(self.chatbot)
        self.listTrainer = ListTrainer(self.chatbot)
        self.query = databaseutil.getMessages()
