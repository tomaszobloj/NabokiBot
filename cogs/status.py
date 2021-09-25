import discord
from discord.ext import commands


class Status(commands.Cog):
    def __init__(self, client):
        self.client = client

    #commands
    #bot latency check
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong!')


def setup(client):
    client.add_cog(Status(client))
