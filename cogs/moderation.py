import discord
from discord.ext import commands

from asyncio import get_event_loop, sleep
from concurrent.futures import ThreadPoolExecutor

from datetime import datetime

client = commands.Bot(command_prefix = commands.when_mentioned_or('!'))

class Moderation(commands.Cog):
    '''Pour toutes les commandes de modérations'''

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    @commands.bot_has_permissions(manage_messages = True)
    async def delete(self, ctx, amount = 99):
        '''Pour supprimer les <amount> derniers messages du salon concerné'''
        await ctx.send(f"{amount} message(s) supprimé(s) dans 5 secondes")
        await sleep(5)
        await ctx.channel.purge(limit = amount + 1)

    @commands.command()
    @commands.has_permissions(kick_members = True)
    @commands.bot_has_permissions(kick_members = True)
    async def kick(self, ctx, member:discord.Member, *, reason):
        '''kick @membre pour une raison donnée'''
        await member.kick(reason = reason)
        await ctx.send(f"{member.name} a été kick de ce serveur")

    @commands.command()
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_permissions(ban_members = True)
    async def ban(self, ctx, member:discord.Member, *, reason):
        '''ban @membre pour une raison donnée'''
        await member.ban(reason = reason)
        await ctx.send(f"{member.name} a été bani de ce serveur (id : {member.id})")

    @commands.command()
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_permissions(ban_members = True)
    async def unban(self, ctx, id_member, *, reason):
        '''permet de dès bannir un membre représenté par son id'''
        member = discord.Object(id = int(id_member))
        await guild.unban(member)
        await ctx.send(f"{member.name} a été enlevé de la liste des banis")

    @commands.command()
    @commands.has_role('Co Fondateur')
    async def logs(self, ctx):
        '''envoi les logs suite aux différentes erreur des commandes'''
        await ctx.send(file = discord.File("./assets/document/bot_logs.txt"))

    @commands.command()
    @commands.has_role('Co Fondateur')
    async def answer(self, ctx, member_id, *, message):
        '''envoi un message privé au membre representé par un id'''
        for guild in self.client.guilds: #the reason why i use this is that I had some client.guilds error
            for member in guild.members:
                if member.id == int(member_id):
                    someone = member
        await someone.send(message)
        await ctx.send('message envoyé !')


def setup(client):
    client.add_cog(Moderation(client))
