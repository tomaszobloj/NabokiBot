import discord, os
from keep_alive import keep_alive
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix="~")

status = discord.Status.online
#activity = discord.Game('Hrum')
activity = cycle([
    '~help', 'prefix ~komenda', 'HRUM', 'Hrum', 'hrum',
    'Pozdrawiam mame Krychy', 'Hrum, gdzie moja marchewka'
])


#events
@client.event
async def on_ready():
    #await client.change_presence(status, activity)
    change_status.start()
    print("Logged in as {0.user}".format(client))


#error handler for none existing commands
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Nie ma takiej komendy.")


#tasks
@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(activity)))


#bot commands
#loading cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


#unloading cogs
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


#reloading cogs
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


#loading files from cogs folder
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#web server
keep_alive()

#bot run
client.run(os.getenv('TOKEN'))
