import discord
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
          
    @commands.command(brief="jokesnya enggres sih (NSFW Beware)",help = "intinya sih jokes, tapi kadang-kadang suka kelewatan emang")
    async def joke(self,ctx):
        embed=discord.Embed(color=0xf10971)
        embed.add_field(name="Ada jokes apa hari ini?",value=jokesulang(self), inline=True)
        embed.set_footer(text="Pengingat Dosa",icon_url=self.bot.user.avatar_url)       
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Joke(bot))