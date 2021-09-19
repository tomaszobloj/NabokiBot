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
@client.command(aliases=['ping', 'Ping', 'PING'])
async def ping(ctx):
    await ctx.send(f'Pong! (round{client.latency * 1000}) ms')


@client.command(aliases=['witam', 'Witam', 'WITAM'])
async def witam(ctx):
    await ctx.send(random.choice(witam_list))


@client.command(aliases=['8ball', '8Ball', '8BALL'])
async def _8ball(ctx, *, question):
    responses = [
        'To pewne.', 'Zdecydowanie tak.', 'Bez wątpienia.',
        'Tak - zdecydowanie.', 'Możesz na tym polegać.',
        'Tak, jak ja to widzę.', 'Najprawdopodobniej.', 'Perspektywa dobra.',
        'Tak.', 'Znaki wskazujące na tak.', 'No jasne że tak.', 'Jeszcze jak.',
        'Odpowiedz niejasno, spróbuj ponownie.', 'Zapytaj ponownie później.',
        'Zapytaj Arka, on Ci podpowie.', 'Zaptyaj Krychy.',
        'Lepiej ci teraz nie mówić.', 'Nie mogę teraz przewidzieć.',
        'Skoncentruj się i zapytaj ponownie.', 'Nie licz na to.',
        'Moja odpowiedź brzmi: nie.', 'Według moich źródeł, nie.',
        'Perspektywa niezbyt dobra.', 'Bardzo wątpliwe.'
    ]
    await ctx.send(
        f'Zapytanie: {question}\nOdpowiedź: {random.choice(responses)}')


#web server
keep_alive()

#bot run
client.run(os.getenv('TOKEN'))
