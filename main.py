import discord
import os
import random
from keep_alive import keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix = "~")

#bot loggin
@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

#web server
keep_alive()

#bot run
client.run(os.getenv('TOKEN'))