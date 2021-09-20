import discord
import random
from discord.ext import commands


guild_list=[]
isi_colek=['hayo, kok lagi buka internet positif ','WOIII ','Assalamualaikum ','Assalamualaika ','**PUSH RANK TEROSS** ','Pantes jomblo, diceluk ga bales ','**KOCOK TERUS TUH BATANGG** ','Bangun woy ayo mulung ','Dih dikit-dikit afk ']
isi_tanya=['Oh ya jelas dong', 'Boleh-boleh', 'Ya','100% setuju','BUETULL','Setuju kali aing','Hmm.. 75% setuju lah','Lebih condong ke setuju sih','Lagi mager, ketik lagi sono','Gausa kepo napa sih','Gamau, lu jahat','Netral ajadah','50-50 dah','Males jawab,mending tidur','Hmm.. lebih ke gak setuju','Orrraa setuju','Jelas gak setuju','G','100% tidak setuju','GA SETUJU FIX VALID NO DEBAT']
isi_gatcha=["Menurut saya sih A",'Condong ke B sih','Menurut bot jawabannya adalah C','Bisa dipastikan D','Mungkin jawabannya E''Udah A aja','Udah B aja','Udah C aja','Udah D aja','Udah E aja','Kayaknya A seh','Kira-kira B','Bisa jadi C','Keliatannya D','Feelingku sih E','Coba jawab A aja','Coba jawab B aja','Coba jawab C aja','Coba jawab D aja','Coba jawab E aja','Susah skip','Gatau keknya, skip','Doa aja, saya gabisa ngeramal :D','Tutup laptop aja','Pusying ane, gatau']
isi_gabut=['pergi mancing','nolep anime aja','buka ig, search @alwinata13, terus follow','traktiran satu angkatan','kerjain laprak','**TIDUR GOBLOK**','malem mingguan sama tangan','tadarus :D','tahajud :D','oh jomblo, pantes gabut','mendaki gunung, lewati lembah','Menonton Video (Terserah biru atau gak)','Streaming kajian','nonton SAO (sumpah wajib ditonton fix valid no debat)','**SIAPA LU SURUH SURUH GUA**','EMANG LO SIAPA','IDIH NYURUH NYURUH','gada saran','mboh','gatau','terserah']

isi_cakepup = [':kissing_heart:',':stuck_out_tongue_closed_eye:',':flushed:',':heart_eyes:',':smiling_face_with_3_hearts:']

isi_cakepdown = [':nerd:',':confounded:',':zipper_mouth:',':face_vomiting:',':sick:']


class Bacotan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
#Melihat Berapa Server Tersambung
    @commands.command(brief="||OWNER ONLY||",pass_context = True)
    
    @commands.is_owner()
    async def guild(self,ctx):
        for guild in self.bot.guilds:
            store=guild.name
            guild_list.append(store)
        await ctx.channel.send(', '.join(guild_list))
        guild_list.clear()

    #Melihat Latency Bot
    @commands.command(brief="untuk melihat jumlah latency dari bot",help = "cie liat help")
    async def ping(self,ctx):
        await ctx.send(f'ngepang-ngeping ae = {round(self.bot.latency * 1000)} ms')

    #Mencolek User
    @commands.command(brief="usage = .colek<@dummy>",help = "cie liat help")
    async def colek(self,ctx,*,orang=str(discord.user)):
        res=random.choice(isi_colek)
        await ctx.channel.send(res+orang)

    #Menjawab Pertanyaan Random
    @commands.command(brief="tanya aja, pasti dijawab ya atau tidak",help = "cie liat help")
    async def tanya(self,ctx,*, question):
        await ctx.channel.send(f'Pertanyaan : {question} \nJawab : {random.choice(isi_tanya)}')

    #Menjawab Pertanyaan Gatcha ABCDE
    @commands.command(brief="untuk kalian yg hopeless (cuma bisa A,B,C,D,E)",help = "cie liat help")
    async def gatcha(self,ctx):
        await ctx.channel.send(random.choice(isi_gatcha))

    #Menjawab Pertanyaan Gabut
    @commands.command(brief="saran untuk kalian yang gabut",help = "cie liat help")
    async def gabut(self,ctx):
        await ctx.channel.send(random.choice(isi_gabut))

    @commands.command(brief="Seberapa keren lu",aliases=['ckp'],help = "Seberapa keren sih elu?")
    async def cakepgasih(self,ctx):
      x = random.randint(1,100)
      embed=discord.Embed(color=0xd4cf35)
      if x > 60 :
        embed.add_field(name="**CAKEPMETER**",value=f"Tingkat kecakepan {ctx.author.mention} adalah {x}/100 {random.choice(isi_cakepup)}", inline=False)
      else :
        embed.add_field(name="** CAKEPMETER **",value=f"Tingkat kecakepan {ctx.author.mention} adalah {x}/100 {random.choice(isi_cakepdown)}", inline=False)
      await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(Bacotan(bot))