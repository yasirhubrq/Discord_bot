import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.command(name='test')
async def test(ctx):
    await ctx.send('pong')

@bot.command(name='loots')
async def loots(ctx):
    await ctx.send('bruh')

@bot.command(name='hello')
async def hello(ctx):
    await ctx.raect('heart')

bot.run('MTI5NTc0NzY2NzcyNDMzNzE1Mw.Gw8h0b.LLQsocsSOt2NvWsFdx0GhP2XgJspiW-r8AKxIE')