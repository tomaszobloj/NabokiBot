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
  await ctx.send('WITAM')

#web server
keep_alive()

#bot run
client.run(os.getenv('TOKEN'))