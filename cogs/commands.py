import discord
import random
from discord.ext import commands

witam_list = [
    "WITAM!", "Witam!", "witam!", "WITAM", "Witam", "witam", "WITAM...",
    "Witam...", "witam...", "Kij Ci w oko", "SIEMA", "Siema", "siema", "ELO",
    "Elo", "elo", "UWAGA KRYCHA MROZI", "Wyobraź sobie że żyjesz w XXI wieku"
]


class Komendy(commands.Cog):
    def __init__(self, client):
        self.client = client

    #witam command
    @commands.command(aliases=['Witam', 'WITAM'])
    async def witam(self, ctx):
        await ctx.send(random.choice(witam_list))

    #8ball command
    @commands.command(aliases=['8ball', '8Ball', '8BALL'])
    async def _8ball(self, ctx, *, question):
        responses = [
            'To pewne.', 'Zdecydowanie tak.', 'Bez wątpienia.',
            'Tak - zdecydowanie.', 'Możesz na tym polegać.',
            'Tak, jak ja to widzę.', 'Najprawdopodobniej.',
            'Perspektywa dobra.', 'Tak.', 'Znaki wskazujące na tak.',
            'No jasne że tak.', 'Jeszcze jak.',
            'Odpowiedz niejasno, spróbuj ponownie.',
            'Zapytaj ponownie później.', 'Zapytaj Arka, on Ci podpowie.',
            'Zaptyaj Krychy.', 'Lepiej ci teraz nie mówić.',
            'Nie mogę teraz przewidzieć.',
            'Skoncentruj się i zapytaj ponownie.', 'Nie licz na to.',
            'Moja odpowiedź brzmi: nie.', 'Według moich źródeł, nie.',
            'Perspektywa niezbyt dobra.', 'Bardzo wątpliwe.'
        ]
        await ctx.send(
            f'Zapytanie: {question}\nOdpowiedź: {random.choice(responses)}')

    #clear command very dangerous
    @commands.command()
    async def clear(self, ctx, amount=2):
        await ctx.channel.purge(limit=amount)


def setup(client):
    client.add_cog(Komendy(client))
