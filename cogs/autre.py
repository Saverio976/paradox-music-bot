import discord
import asyncio
import datetime, pytz

from discord.ext import commands

client = commands.Bot(command_prefix = commands.when_mentioned_or('!'))

class Other(commands.Cog):
    '''Une category pour les commandes STF (sans thème fix)'''

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['hm', 'heure_monde'])
    async def HeureMonde(self, ctx):
        """Pour connaitre l'heure des autres pays dans le monde"""
        if ctx.channel.id == 712702579133644850: #le channel flood
            L_hm_nom = ['France','Fr_Mayotte',
                        'Australia','USA_New_York',
                        'USA_Los_Angeles','Italy',
                        'Egypt','India',
                        'China_Shanghai','Japon',
                        'Affrique_du_sud']
            L_hm_heure = [
                datetime.datetime.now(pytz.timezone('Europe/Paris')).strftime("%d %m %Y  %H:%M:%S"),
                datetime.datetime.now(pytz.timezone('Indian/Mayotte')).strftime("%d %m %Y  %H:%M:%S"),
                datetime.datetime.now(pytz.timezone('Australia/Sydney')).strftime("%d %m %Y  %H:%M:%S"),
                datetime.datetime.now(pytz.timezone('America/New_York')).strftime("%d %m %Y  %H:%M:%S"),
                datetime.datetime.now(pytz.timezone('America/Los_Angeles')).strftime("%d %m %Y  %H:%M:%S"),
                datetime.datetime.now(pytz.timezone('Europe/Rome')).strftime("%d %m %Y  %H:%M:%S"),
                datetime.datetime.now(pytz.timezone('Africa/Cairo')).strftime("%d %m %Y  %H:%M:%S"),
                datetime.datetime.now(pytz.timezone('Asia/Kolkata')).strftime("%d %m %Y  %H:%M:%S"),
                datetime.datetime.now(pytz.timezone('Asia/Shanghai')).strftime("%d %m %Y  %H:%M:%S"),
                datetime.datetime.now(pytz.timezone('Asia/Tokyo')).strftime("%d %m %Y  %H:%M:%S"),
                datetime.datetime.now(pytz.timezone('Africa/Johannesburg')).strftime("%d %m %Y  %H:%M:%S")]
            for i in range(len(L_hm_nom)):
                await ctx.send(L_hm_nom[i]+" -> "+L_hm_heure[i])
                await asyncio.sleep(1)

    @commands.command(aliases=['ayo','hi','salut','bonjour'],case_intensitive=True)
    async def hello(self, ctx):
        '''Te réponds bonjours.'''
        await ctx.send(f'Bonjour petit humain !\nJe sais que tu te nommes : {ctx.author.name}')

    @commands.command()
    async def carapuce(self, ctx):
        '''Montre sa réaction en entendant ce mot'''
        await ctx.send('Beuuuuurk')

    @commands.command()
    async def emb(self, ctx):
        '''Un truc fun à faire une fois dans sa vie.'''
        em = discord.Embed(title="titre", description="desc", colour=0xFF0000, timestamp=ctx.message.created_at)
        em.add_field(name="Un field", value="Youpi", inline=True)
        em.add_field(name="Un autre field", value="o/", inline=True)
        em.add_field(name="Un field pas sur la même ligne", value="grâce au 'inline'",inline=False)
        em.set_author(name="Un gars super",icon_url=ctx.author.avatar_url)
        em.set_footer(text="Sur un super serveur", icon_url=ctx.guild.icon_url)
        em.set_image(url="https://cdn.discordapp.com/attachments/710490015087722506/738743933105995876/salameche_2.png")
        await ctx.send(embed=em)

    @commands.command(aliases=['sn','StopNow','stopNow','Stopnow'])
    @commands.has_role('Co Fondateur')
    async def stopnow(self, ctx):
        '''uniquement pour ceux ayant le role Co Fondateur (permet de deconnecter le bot)'''
        await client.logout()


def setup(client):
    client.add_cog(Other(client))
