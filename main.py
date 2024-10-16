#importing all the modules and libraries
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
#to load the token from .env file
load_dotenv

TOKEN = os.getenv('DISCORD_TOKEN')
#giving permission to bot to read and write messages
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)
#creating commands
@bot.command(name='test')
async def test(ctx):
    await ctx.send('pong')

@bot.command(name='loots')
async def loots(ctx):
    await ctx.send('bruh')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.raect('heart')
#bot token and runn
bot.run('')
