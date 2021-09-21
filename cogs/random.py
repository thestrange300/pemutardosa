import discord
import random
from discord.ext import commands
import requests
import json

isi_gatcha=["Menurut saya sih A",'Condong ke B sih','Menurut bot jawabannya adalah C','Bisa dipastikan D','Mungkin jawabannya E''Udah A aja','Udah B aja','Udah C aja','Udah D aja','Udah E aja','Kayaknya A seh','Kira-kira B','Bisa jadi C','Keliatannya D','Feelingku sih E','Coba jawab A aja','Coba jawab B aja','Coba jawab C aja','Coba jawab D aja','Coba jawab E aja','Susah skip','Gatau keknya, skip','Doa aja, saya gabisa ngeramal :D','Tutup laptop aja','Pusying ane, gatau']
isi_gabut=['pergi mancing','nolep anime aja','buka ig, search @alwinata13, terus follow','traktiran satu angkatan','kerjain laprak','**TIDUR GOBLOK**','malem mingguan sama tangan','tadarus :D','tahajud :D','oh jomblo, pantes gabut','mendaki gunung, lewati lembah','Menonton Video (Terserah biru atau gak)','Streaming kajian','nonton SAO (sumpah wajib ditonton fix valid no debat)','**SIAPA LU SURUH SURUH GUA**','EMANG LO SIAPA','IDIH NYURUH NYURUH','gada saran','mboh','gatau','terserah']

isi_cakepup = [':kissing_heart:',':flushed:',':heart_eyes:',':smiling_face_with_3_hearts:']

isi_cakepdown = [':nerd:',':confounded:',':zipper_mouth:',':face_vomiting:',':sick:']

def randomuser(self):
  url = "https://random-user.p.rapidapi.com/getuser"
  headers = {
      'x-rapidapi-host': "random-user.p.rapidapi.com",
      'x-rapidapi-key': "2fafd4f798mshfa65e7f9fcee968p1854d6jsnf24f4300e32b"
      }
  req = requests.get(url, headers=headers)
  y = req.text
  z = json.loads(y)
  return (z)

def reloadru(self):
  global ru
  ru = randomuser(0)

ru = randomuser(0)

def excuse(self):
  req = requests.get("https://api.devexcus.es/")
  y= req.json()
  return (y)

def reloadex(self):
  global ex
  ex = excuse(0)

ex = excuse(0)

class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Menjawab Pertanyaan Gatcha ABCDE
    @commands.command(brief="untuk kalian yg hopeless (cuma bisa A,B,C,D,E)",help = "ya buat gatcha, apalagi")
    async def gatcha(self,ctx):
        await ctx.channel.send(random.choice(isi_gatcha))

    #Menjawab Pertanyaan Gabut
    @commands.command(brief="saran untuk kalian yang gabut",help = "guabut betul kalian sampe cari disini")
    async def gabut(self,ctx):
        await ctx.channel.send(random.choice(isi_gabut))

    @commands.command(brief="usage = wur <text> ",help = "What's Ur Robot bakalan nampilin robot random sesuai textmu.\n Usage = **wur <text>**")
    async def wur(self,ctx,*,question):
        embed=discord.Embed(title=f"Robot dari {question}",color=0xff4000)
        tmp= f"https://robohash.org/{question}"
        embed.set_image(url = tmp)
        embed.set_footer(text="Pengingat Dosa",icon_url=self.bot.user.avatar_url) 
        await ctx.channel.send(embed=embed) 

    #RANDOM USER GENERATOR
    @commands.command(brief="generate random user",aliases = ['ru'], help = "generate sebuah profil secara random\nAlias = **ru**")
    async def randuser(self,ctx):
        embed=discord.Embed(title="User Berhasil Dibuat :",description=f"**Nama** : {ru['results'][0]['name']['title']} {ru['results'][0]['name']['first']} {ru['results'][0]['name']['last']}\n**Gender** : {ru['results'][0]['gender']} \n**Alamat** : {ru['results'][0]['location']['street']['name']} {ru['results'][0]['location']['street']['number']}, {ru['results'][0]['location']['city']}, {ru['results'][0]['location']['state']}, {ru['results'][0]['location']['country']}\n**Kode Pos** : {ru['results'][0]['location']['postcode']}\n**Email** : {ru['results'][0]['email']}\n**Username** : {ru['results'][0]['login']['username']}\n**Password** : {ru['results'][0]['login']['password']}\n**Telp Rumah** : {ru['results'][0]['phone']}\n**Telp HP** : {ru['results'][0]['cell']}", color=0xff4000)
        embed.set_image(url = ru['results'][0]['picture']['large'])
        embed.set_footer(text="Pengingat Dosa",icon_url=self.bot.user.avatar_url)
        reloadru(self) 
        print (ru)
        await ctx.channel.send(embed=embed)  

    #CAKEP GA SEH
    @commands.command(brief="Seberapa keren lu",aliases=['ckp'],help = "Seberapa keren sih elu?\nAlias = **ckp**")
    async def cakepgasih(self,ctx):
      x = random.randint(1,100)
      embed=discord.Embed(color=0xff4000)
      if x > 60 :
        embed.add_field(name="**CAKEPMETER**",value=f"Tingkat kecakepan {ctx.author.mention} adalah {x}/100 {random.choice(isi_cakepup)}", inline=False)
      else :
        embed.add_field(name="** CAKEPMETER **",value=f"Tingkat kecakepan {ctx.author.mention} adalah {x}/100 {random.choice(isi_cakepdown)}", inline=False)
      await ctx.channel.send(embed=embed)

    @commands.command(brief="butuh alasan?? ini solusinya", aliases = ['ex'],help = "butuh alasan?? ini solusinya\nAlias : **ex**")
    async def excuse(self,ctx):
        embed=discord.Embed(title=f"Alasan :",description=f"{ex['text']}", color=0xff4000)
        embed.set_footer(text="Pengingat Dosa",icon_url=self.bot.user.avatar_url)
        reloadex(self)
        await ctx.channel.send(embed=embed)    

def setup(bot):
    bot.add_cog(Random(bot))