import discord
from discord.ext import commands
from botmodoro_token import *  # importing the token from a separate file

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!pomo ', intents=intents)

@client.event
async def on_ready():
    print('Botmodoro is now ready for use!')
    print('*******************************')

@client.command()
async def hello(ctx):
    await ctx.send('Hi!')

@client.command()
async def goodbye(ctx):
    await ctx.send('See you!')

@client.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('You are not in a voice channel. You must be in a voice channel to run this command.')

@client.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send('Leaving the voice channel.')
    else:
        await ctx.send('I am not in a voice channel...')

client.run(bot_token)
