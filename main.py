import discord
import os
import requests
import json
import random
from replit import db

client = discord.Client()

word_list = ["WITAM", "witam", "KRYCHA", "krycha"]
starters = ["WITAM", "CO", "ALE MROZI"]

#bot random quote
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

#adding words 1
def update_words(word_list):
  if "words" in db.keys():
    words = db["words"]
    words.appen(word_list)
    db["words"] = words
  else:
    db["words"] = [word_list]

#deleting words 1
def delete_words(index):
  words = db["words"]
  if len(words) > index:
    del words[index]
    db["words"] = words

@client.event
async def on_message(message):
    if message.author == client.user:
      return

    msg = message.content

    if msg.startswith('$inspire'):
      quote = get_quote()
      await message.channel.send(quote)

    #1
    options = starters
    if "words" in db.keys():
      options = options + db["words"]

    if any(word in msg for word in word_list):
      await message.channel.send(random.choice(options))

    #1
    if msg.startswith("$new"):
      word_list = msg.split("$new ",1)[1]
      update_words(word_list)
      await message.channel.send("New word added!")

    #1
    if msg.startswith("$del"):
      words = []
      if "words" in db.keys():
        index = msg.split("$del",1)[1]
        delete_words(index)
        words = db["words"]
      await message.channel.send(words)


#bot loggin
@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


#bot saying witam
#@client.event
#async def on_message(message):
#    if message.author == client.user:
#      return
#
#    if message.content.startswith('WITAM'):
#      await message.channel.send('WITAM!')

##bot run
client.run(os.getenv('TOKEN'))