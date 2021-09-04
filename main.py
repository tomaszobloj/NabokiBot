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
              "WITAM, co tam u mamy Krycha?",
              "Kij Ci w oko",
              "SIEMA",
              "Siema",
              "siema",
              "ELO",
              "Elo",
              "elo",
              "UWAGA KRYCHA MROZI",
              "Wyobraź sobie że żyjesz w XXI wieku"]

krycha_list = ["KRYCHA",
               "Tosia do nogi",
               "Krycha chuj",
               "Bardzo tania postytutka w podeszłym wieku",
               "Chluśniem bo uśniem",
               "Ma być studniówka",
               "To kiedy zdalne?",
               "Mam alarm",
               "Kupiłem Julce misia",
               "Jebać Kubusia",
               "Jebać Szymona",
               "KURWA",
               "KURWA KURWA KURWA",
               "KURWA to twoja stara",
               "Ide do sklepu po cole",
               "Poproszę kebaba bez warzyw",
               "Poproszę kebaba tylko z mięsem",
               "To co 10 złotych na paliwo",
               "Oddawaj Termite",
               "???",
               "Matme robie",
               "Ucze się",
               "Kawa za 2 złote u pana Adriana",
               "XD",
               "Grasz w fortnite",
               "japierdole",
               "ja odpadam dzis na granie",
               "Mam mokre włosy",
               "XDDDDDDDD",
               "gramy w reinbowa?"]

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
    
    if message.content.startswith('KRYCHA'):
        await message.channel.send(random.choice(krycha_list))

#web server
keep_alive()

#bot run
client.run(os.getenv('TOKEN'))