import discord
import os
import random
from keep_alive import keep_alive

client = discord.Client()
witam_list = ["WITAM!",
              "Witam!",
              "witam!",
              "WITAM",
              "Witam",
              "witam",
              "WITAM...",
              "Witam...",
              "witam...",
              "Kij Ci w oko",
              "SIEMA",
              "Siema",
              "siema",
              "ELO",
              "Elo",
              "elo",
              "UWAGA KRYCHA MROZI",
              "Wyobraź sobie że żyjesz w XXI wieku"]

#bot loggin
@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

#bot messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('WITAM'):
        await message.channel.send(random.choice(witam_list))

#web server
keep_alive()

#bot run
client.run(os.getenv('TOKEN'))