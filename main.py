import discord
import os
from keep_alive import keep_alive

client = discord.Client()

#bot loggin
@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

#bot saying witam
@client.event
async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('WITAM'):
      await message.channel.send('WITAM!')

#web server
keep_alive()
#bot run
client.run(os.getenv('TOKEN'))