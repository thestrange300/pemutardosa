from discord.ext import commands

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re


def jokesulang(self):
  req = Request("https://v2.jokeapi.dev/joke/Any?format=txt  ")
  html_page = urlopen(req)
  soup = BeautifulSoup(html_page, "html.parser")
  html_text = soup.get_text()
  return html_text

class Joke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
          
    @commands.command(brief="jokesnya enggres sih",help = "cie liat help")
    async def joke(self,ctx):    
        await ctx.channel.send(jokesulang(self))

def setup(bot):
    bot.add_cog(Joke(bot))