import discord
import random
from discord.ext import commands


isi_colek=['hayo, kok lagi buka internet positif ','WOIII ','Assalamualaikum ','Assalamualaika ','**PUSH RANK TEROSS** ','Pantes jomblo, diceluk ga bales ','**KOCOK TERUS TUH BATANGG** ','Bangun woy ayo mulung ','Dih dikit-dikit afk ']
isi_tanya=['Oh ya jelas dong', 'Boleh-boleh', 'Ya','100% setuju','BUETULL','Setuju kali aing','Hmm.. 75% setuju lah','Lebih condong ke setuju sih','Lagi mager, ketik lagi sono','Gausa kepo napa sih','Gamau, lu jahat','Netral ajadah','50-50 dah','Males jawab,mending tidur','Hmm.. lebih ke gak setuju','Orrraa setuju','Jelas gak setuju','G','100% tidak setuju','GA SETUJU FIX VALID NO DEBAT']

class Bacotan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Mencolek User
    @commands.command(brief="usage = .colek<@dummy>",help = "Mencolek user lainnya\nUsage : **colek<@dummy>**")
    async def colek(self,ctx,*,orang=str(discord.user)):
        res=random.choice(isi_colek)
        await ctx.channel.send(res+orang)

    #Menjawab Pertanyaan Random
    @commands.command(brief="tanya aja, pasti dijawab ya atau tidak",help = "Tanya aja, pasti dijawab ya atau tidak\nUsage : **tanya <pertanyaan>**")
    async def tanya(self,ctx,*, question):
        await ctx.channel.send(f'Pertanyaan : {question} \nJawab : {random.choice(isi_tanya)}')


def setup(bot):
    bot.add_cog(Bacotan(bot))