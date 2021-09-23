import discord
from discord.ext import commands

guild_list =[]

class Other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Melihat Latency Bot
    @commands.command(brief="untuk melihat jumlah latency dari bot",help = "Melihat jumlah latency dari bot")
    async def ping(self,ctx):
        await ctx.send(f'ngepang-ngeping ae, {round(self.bot.latency * 1000)} ms duh')

#Melihat Berapa Server Tersambung
    @commands.command(brief="||OWNER ONLY||",pass_context = True)
    
    @commands.is_owner()
    async def guild(self,ctx):
        for guild in self.bot.guilds:
            store=guild.name
            guild_list.append(store)
        await ctx.channel.send(', '.join(guild_list))
        guild_list.clear()

#### INFO SERVER ####
    @commands.command()
    async def info(self,ctx):
        embed = discord.Embed(title=f"{ctx.guild.name}", description="** **", color=0xffffff)
        embed.add_field(name="Server dibuat pada", value=f"{ctx.guild.created_at}")
        embed.add_field(name="Pemilik Server", value=f"{ctx.guild.owner}")
        embed.add_field(name="Wilayah Server", value=f"{ctx.guild.region}")
        embed.add_field(name="ID Server", value=f"{ctx.guild.id}")
        embed.set_thumbnail(url=ctx.guild.icon_url)

        await ctx.channel.send(embed=embed)

    @commands.command(brief="panjang umur kebebasan",help = "Panjang umur kebebasan!!!!")
    async def ip(self,ctx):
        embed = discord.Embed(title=f"PANJANG UMUR SAYAP KEBEBASAN", description="Puja banteng ajaib", color=0xff0505)
        embed.set_image(url = 'https://awsimages.detik.net.id/community/media/visual/2019/04/15/0ed3f774-4eb9-4275-b7f2-9b514f9676e9_43.jpeg?w=700&q=90')
        await ctx.channel.send(embed=embed) 
        
def setup(bot):
    bot.add_cog(Other(bot))