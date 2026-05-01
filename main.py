import discord as dc
from discord.ext import commands
import random
import scrapss
TOKEN = '' #replace with your bot token
__init__ = __name__
intents = dc.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)
#this event is used to print a message when the bot is ready and logged in
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
#this command is used to get a random meme from the imgflip api and send it as an embed in the discord channel
@client.command()
async def meme(ctx):
    embed = dc.Embed(title="Here's a meme for you!",color=0x00ff00)
    embed.set_image(url=scrapss.get_meme())
    await ctx.send(embed=embed)
#this command is used to get the current players in the game and their details
@client.command()
async def players(ctx):
    embed2 = dc.Embed(title="Current Players in Game",description=scrapss.player_det(),color=0x0000ff)
    embed2.add_field(name="", value="", inline=False)
    await ctx.send(embed=embed2)
#this command is used to get the location of an IP address
@client.command()
async def locate(ctx, ip_address):
    location_info = scrapss.ip_locate(ip_address)
    await ctx.send(f"Location info for IP {ip_address}: {location_info}")


client.run(TOKEN)
