import discord
from discord.ext import commands

from asyncio import get_event_loop, sleep
from concurrent.futures import ThreadPoolExecutor

from datetime import datetime

client = commands.Bot(command_prefix = commands.when_mentioned_or('!'))

class Moderation(commands.Cog):

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
        await member.kick(reason = reason)
        await ctx.send(f"{member.name} a été kick de ce serveur")

    @commands.command()
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_permissions(ban_members = True)
    async def ban(self, ctx, member:discord.Member, *, reason):
        await member.ban(reason = reason)
        await ctx.send(f"{member.name} a été bani de ce serveur")

    @commands.command()
    @commands.has_permissions(ban_members = True)
    @commands.bot_has_permissions(ban_members = True)
    async def unban(self, ctx, id_member:int(), *, reason):
        member = discord.Object(id = id_member)
        await guild.unban(member)
        await ctx.send(f"{member.name} a été enlevé de la liste des banis")

    def is_bot_owner(ctx):
        return ctx.author.id == 425965177616334849

    @commands.command()
    @commands.check(is_bot_owner)
    async def logs(self, ctx):
        await ctx.send(file = discord.File("./assets/document/bot_logs.txt"))

    @commands.command()
    @commands.check(is_bot_owner)
    async def answer(self, ctx, member_id, *, message):
        for guild in self.client.guilds: #the reason why i use this is that I had some client.guilds error
            for member in guild.members:
                if member.id == int(member_id):
                    someone = member
        await someone.send(message)
        await ctx.send('message envoyé !')


def setup(client):
    client.add_cog(Moderation(client))
