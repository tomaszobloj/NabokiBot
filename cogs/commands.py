import discord
import random
from discord.ext import commands

witam_list = [
    "WITAM!", "Witam!", "witam!", "WITAM", "Witam", "witam", "WITAM...",
    "Witam...", "witam...", "Kij Ci w oko", "SIEMA", "Siema", "siema", "ELO",
    "Elo", "elo", "UWAGA KRYCHA MROZI", "Wyobraź sobie że żyjesz w XXI wieku"
]

krycha_list = [
    "KRYCHA", "Tosia do nogi", "Krycha chuj",
    "Bardzo tania postytutka w podeszłym wieku", "Chluśniem bo uśniem",
    "Ma być studniówka", "To kiedy zdalne?", "Mam alarm",
    "Kupiłem Julce misia", "Jebać Kubusia", "Jebać Szymona", "KURWA",
    "KURWA KURWA KURWA", "KURWA to twoja stara", "Ide do sklepu po cole",
    "Poproszę kebaba bez warzyw", "Poproszę kebaba tylko z mięsem",
    "To co 10 złotych na paliwo", "Oddawaj Termite", "???", "Matme robie",
    "Ucze się", "Kawa za 2 złote u pana Adriana", "XD", "Grasz w fortnite",
    "japierdole", "ja odpadam dzis na granie", "Mam mokre włosy", "XDDDDDDDD",
    "gramy w reinbowa?", "Nie wkurwiaj mnie", "Tomek nie wkurwiaj mnie",
    "Masz to usunąć", "KURWA", "Kurwa", "kurwa", "Skurwysynu", "Widziałeś grupe"
]

tomasz_list = [
    "WITAM", "Japierdole jesteś frajer", "no xd", "Jebać Kryche",
    "Gdzie jest krizdow", "AHA", "aha", "Aha", "Gramy w Deep Rock'a?", "ROCK AND STONE!", 
    "Rock and Stone!", "Gdzie jest krizdow?"
]

arek_list = [
    "Ojacie", "Kij Ci w oko", "Wiadro", "Co wiadro 1:0 grasz dalej?", "?QUIERES?", 
    "A wiedziałeś, że ...", "O kur...", "Kij", "kij","aha", "AHA", "WAT", "ROCK AND STONE!", 
    "Rock and Stone!"
]

oskar_list = [
  "Topur KURWA topory", "Pierdol mnie", "Dziękuje", "ROCK AND STONE!", "Rock and Stone!",
  "Ale ty mi sie kurwa podobasz", "Gdzie jest krizdow?"
]

konik_list = [
  "WITAM", "Ide sie wysrać zw", "Arek chce banana", "Dziękuje", '~~mlaskanie~~', '~~bek~~', 
  "ROCK AND STONE!", "Rock and Stone!"
]


class Komendy(commands.Cog):
    def __init__(self, client):
        self.client = client

    #witam command
    @commands.command(aliases=['Witam', 'WITAM'])
    async def witam(self, ctx):
        await ctx.send(random.choice(witam_list))

    #krycha command
    @commands.command(aliases=['Krycha', 'KRYCHA'])
    async def krycha(self, ctx):
        await ctx.send(random.choice(krycha_list))

    #tomasz command
    @commands.command(aliases=['Tomasz', 'TOMASZ'])
    async def tomasz(self, ctx):
        await ctx.send(random.choice(tomasz_list))

    #arek command
    @commands.command(aliases=['Arek', 'AREK'])
    async def arek(self, ctx):
        await ctx.send(random.choice(arek_list))

    #oskar command
    @commands.command(aliases=['Oskar', 'OSKAR'])
    async def oskar(self, ctx):
        await ctx.send(random.choice(oskar_list))

    #konik command
    @commands.command(aliases=['Konik', 'KONIK'])
    async def konik(self, ctx):
        await ctx.send(random.choice(konik_list))

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
            'Perspektywa niezbyt dobra.', 'Bardzo wątpliwe.', 'Nope.', 
            'NOPE.', "Wypierdalaj z takim pytaniem", "Pojebało Cię?", 
            "Napewno nie", "Zdecydowane nie", "NIE", "nein", "NEIN", 
            "ani náhodou", "Ei", "नहीं", "Pas", "Pass"
        ]
        await ctx.send(
            f'Zapytanie: {question}\nOdpowiedź: {random.choice(responses)}')

    #8ball error handler
    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Zapytaj o coś. ~8ball [pytanie].")

    #clear command very dangerous
    #@commands.command()
    #async def clear(self, ctx, amount : int):
    #    await ctx.channel.purge(limit=amount)

    #clear error handler
    #@clear.error
    #async def clear_error(self, ctx, error):
    #  if isinstance(error, commands.MissingRequiredArgument):
    #    await ctx.send("Podaj wartość. ~clear [wartość].")


def setup(client):
    client.add_cog(Komendy(client))
