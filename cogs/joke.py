import discord
from discord.ext import commands
import requests
import json

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re


def jokesulang(self):
  req = Request("https://v2.jokeapi.dev/joke/Any?format=txt  ")
  html_page = urlopen(req)
  soup = BeautifulSoup(html_page, "html.parser")
  html_text = soup.get_text()
  return html_text

def dadjoke(self):
  req = requests.get("https://icanhazdadjoke.com/", headers = {"Accept": "application/json"})
  y= req.json()
  return (y['joke'])

def redditmeme(self):
  req = requests.get("https://meme-api.herokuapp.com/gimme")
  y= req.json()
  return (y)

def reloadsr(self):
  global sr
  sr = redditmeme(0)

sr = redditmeme(0)

class Joke(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #JOKES       
    @commands.command(brief="jokesnya enggres sih (NSFW Beware)",aliases=['jk'],help = "intinya sih jokes, tapi kadang-kadang suka kelewatan emang")
    async def joke(self,ctx):
        embed=discord.Embed(color=0x8000ff)
        embed.add_field(name="Jokes hari ini :",value=jokesulang(self), inline=True)
        await ctx.channel.send(embed=embed)
        
##### UNTUK FOOTER YG EPIC #####
        # embed.set_footer(text="Pengingat Dosa",icon_url=self.bot.user.avatar_url) 

    #Menjawab Pertanyaan Random
    @commands.command(brief="jokes bapack bapack",aliases=['dj'],help = "isinya cuma jokes bapack-bapack sih")
    async def dadjoke(self,ctx):
        embed=discord.Embed(color=0x8000ff)
        embed.add_field(name="Jokes bapack hari ini :",value=dadjoke(self), inline=True)     
        await ctx.channel.send(embed=embed)  

    @commands.command(brief="meme fresh dari reddit",help = "ya isinya meme dari reddit")
    async def meme(self,ctx):
        embed=discord.Embed(title=sr['title'],description=f"**Subreddit** : {sr['subreddit']}", color=discord.Color.pink)
        embed.set_image(url = sr['url'])
        embed.set_footer(text=f" 👍 {sr['ups']}")
        reloadsr(self)
        await ctx.channel.send(embed=embed)    
        

def setup(bot):
    bot.add_cog(Joke(bot))