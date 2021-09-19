import discord
import os
import random
from keep_alive import keep_alive
#from discord.ext import commands

client = discord.Client()
#client = commands.Bot(command_prefix = ".")

help_list = """:pig: Lista komend bota NABOKI: 
:arrow_forward: HELP - komenda pomocy
:arrow_forward: WITAM - przywitanie się z NABOKI, który odpowiada pozdowieniem z listy słów
:arrow_forward: KRYCHA - komenda wyłączona"""

witam_list = [
    "WITAM!", "Witam!", "witam!", "WITAM", "Witam", "witam", "WITAM...",
    "Witam...", "witam...", "Kij Ci w oko", "SIEMA", "Siema", "siema", "ELO",
    "Elo", "elo", "UWAGA KRYCHA MROZI", "Wyobraź sobie że żyjesz w XXI wieku"
]

#bot loggin
@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

#bot commands
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    #async def displayembed():
    #  embed = discord.Embed(title='Title',
    #                        description='Descxription',
    #                        colour=discord.Colour.red())
    #
    #  embed.set_footer(text='This is a footer.')
    #  embed.set_author(name='TOMASZ')
    #  embed.add_field(name='Field Name', value='Field Value', inline=False)
    #  embed.add_field(name='Field Name1', value='Field Value', inline=True)
    #  embed.add_field(name='Field Name2', value='Field Value', inline=True)

    if message.content.startswith('HELP'):
        await message.channel.send(help_list)

    if message.content.startswith('WITAM'):
        await message.channel.send(random.choice(witam_list))

    #if message.content.startswith('POMOC'):
    #    await message.channel.send(displayembed())

#web server
keep_alive()

#bot run
client.run(os.getenv('TOKEN'))