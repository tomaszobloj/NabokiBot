import discord
import os
import random
from keep_alive import keep_alive
from discord.ext import commands

client = commands.Bot(command_prefix="~")

witam_list = [
    "WITAM!", "Witam!", "witam!", "WITAM", "Witam", "witam", "WITAM...",
    "Witam...", "witam...", "Kij Ci w oko", "SIEMA", "Siema", "siema", "ELO",
    "Elo", "elo", "UWAGA KRYCHA MROZI", "Wyobraź sobie że żyjesz w XXI wieku"
]


#bot loggin
@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


#member joined a server
@client.event
async def on_member_join(member):
    print(f'{member} dołączył.')


#member left a server
@client.event
async def on_member_remove(member):
    print(f'{member} odszedł.')


#bot commands
@client.command()
async def WITAM(ctx):
    await ctx.send(random.choice(witam_list))

@client.command()
async def PING(ctx):
    await ctx.send(f'PONG! (round{client.latency * 1000}) ms')


#web server
keep_alive()

#bot run
client.run(os.getenv('TOKEN'))
