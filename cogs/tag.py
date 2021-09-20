from discord.ext import commands
import random

x = ['asu', 'jing', 'ntol', 'mek', 'cok', 'mbut', 'meki', 'gsat', 'stis', 'sat', 'pantek', 'entot', 'perek',
'oblok', 'empek', 'mbot', 'kntl', 'anjg', 'jnck', 'bgst', 'asw', 'jmbt', 'pntek', 'entod', 'glbk','njeng','sange']

isi_quote = [
'Astaghfirullah lambene ',
'Cuocote ',
'HEH LAMBENE ',
'ENAKNO TEROS MISUH E ',
'Pantes jomblo, cocote koyok ngene ',
'Deloken iki lo rek kelakuan ',
'LOH, gamalu diliat roqib atid ? ',
'Ancen kelakuan ',
'**TOBAT LAH KISANAK**',
'**PUANCET AE**']

y = ['mikum','samlekum','assalam','samlekom',]
z = ['ngap','lapo']
isi_salam=['Waalaikumsalam..',
'Waalaikumsalam.. duh adem banget',
'Waalaikumsalam.. tumben bicaranya baik-baik',
'Waalaika',
'Waalaikumsalam.. 👍 buat anda']
isi_ngapain=['lagi ngaji duong..',
'lagi main gundu itu',
'lagi dipanggil emaknya',
'lagi ke kosan pacarnya',
'lagi overthinking di pojokan kamar',
'lagi menatap masa depan bersamamu UwU',
'**DAH GAUSAH DIGANGGU NAPA**',
'lagi beliin eskrim kali',
'lagi menjelma menjadi kyuubi',
'lagi jemput kamu, coba ke depan rumah',
'hmmm.. lagi buka VPN kali xixixi',
'lagi jadi wali nikahmu, tapi kalo gaada diganti ST12 aja gapapa **xixixi ngakak abiezz ckuakss**',
'lagi mimpiin masa depan bersamamu']


class tag(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.bot.user:
            pass

        messageContent = str.casefold(message.content)
        if len(messageContent) > 2:
            for String in x:
                if String in messageContent:
                    response = random.choice(isi_quote)
                    await message.channel.send(response+message.author.mention)

        messageContent = str.casefold(message.content)
        if len(messageContent) > 3:
            for String in z:
                if String in messageContent:
                    response=random.choice(isi_ngapain)
                    await message.channel.send(response)

        messageContent = str.casefold(message.content)
        if len(messageContent) > 2:
            for String in y:
                if String in messageContent:
                    response=random.choice(isi_salam)
                    await message.channel.send(response)

        messageContent1= str.casefold(message.content)
        if messageContent1 == 'tes':
            await message.channel.send('tis')

        mention = f'<@!{self.bot.user.id}>'
        if mention in message.content:
            await message.channel.send('ape lu ngetag-ngetag')

        mention_owner = '429591735237214230'
        if mention_owner in message.content:
            await message.channel.send('gausa tag owner gua lu')


def setup(bot):
    bot.add_cog(tag(bot))