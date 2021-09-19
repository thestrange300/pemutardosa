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

bot = commands.Bot(command_prefix=',')

#Inisialisasi Bot
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print('Servers connected to:')
    for guild in bot.guilds:
        print(guild.name)
    # Setting `Streaming ` status
    await bot.change_presence(activity=discord.Streaming(name="dosa-dosa kalian 👼 ", url='https://www.youtube.com/watch?v=bmSyq0mBn54'))

keep_alive.keep_alive()

#LOAD COGS
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')
    
  else:
    print(f'Unable to load {filename[:-3]}')

bot.run(TOKEN, bot=True, reconnect=True)