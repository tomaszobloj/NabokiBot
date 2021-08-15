import discord
from discord.ext import commands
import youtube_dl
import os
from keep_alive import keep_alive

client = commands.Bot(command_prefix="!")

#bot play
@client.command()
async def graj(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Jeszcze gram hrum")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='bot')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {'format': 'bestaudio/best','postprocessors': 
      [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192',}],}
      
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))

#bot leave
@client.command()
async def sio(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Nie ma mnie na kanele hrum")

#music pause
@client.command()
async def pauza(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Nic nie gram hrum")

#music resume
@client.command()
async def dalej(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Nie ma pauzy hrum")

#music stop
@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

#web server
keep_alive()

#bot run
client.run(os.getenv('TOKEN'))