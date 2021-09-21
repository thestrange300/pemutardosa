import os
import asyncio
import functools
import itertools
import math
import random
import keep_alive

import discord
import youtube_dl
from async_timeout import timeout
from discord.ext import commands

TOKEN = os.environ['DISCORD_TOKEN']

#### LIST COG ####
lc = ['Music','Random','Joke','Bacotan','Other']

#### CUSTOM HELP COMMAND ####
class MyHelpCommand(commands.HelpCommand):
  def __init__(self):
    super().__init__()

  async def send_bot_help(self,mapping):
    embed=discord.Embed(color=0xe1ff00)
    embed.add_field(name="List Command",value="**  **",inline=False)
    for i in range(5) :
      x = bot.get_cog(lc[i])
      commands= x.get_commands()
      y = [c.name for c in commands ]
      if 'guild' in y : 
        y.remove('guild')
      z= ['`{0}'.format(i) for i in  y]
      a = ['{0}` '.format(i) for i in  z]
      embed.add_field(name=f"{x.qualified_name}",value=f"{' '.join(a)}",inline = False)
    await self.get_destination().send(embed=embed)

  async def send_command_help(self,command):
    embed=discord.Embed(color=0xe1ff00)
    embed.add_field(name=f"{command.name}",value=f"{command.help}",inline = False)
    await self.get_destination().send(embed=embed)

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='pd ',help_command = MyHelpCommand(),intents=intents)

####BOT STARTUP ####
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print('Servers connected to:')
    for guild in bot.guilds:
        print(guild.name)
    # Setting `watching` status
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="pd help"))  

keep_alive.keep_alive()

#### LOAD COGS ####
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')
    
  else:
    print(f'Unable to load {filename[:-3]}')



bot.run(TOKEN, bot=True, reconnect=True)