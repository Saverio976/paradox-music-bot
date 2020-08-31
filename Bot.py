import discord

import os

from assets.module import data

from discord.ext import commands

client = commands.Bot(command_prefix = commands.when_mentioned_or('!'))

####
# Partie Extension
####
@client.command()
@commands.has_role('aprouvé-par-salamèche-II')
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send("effectué")

@client.command()
@commands.has_role('aprouvé-par-salamèche-II')
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send("effectué")

@client.command()
@commands.has_role('aprouvé-par-salamèche-II')
async def reload(ctx, extension):
    try:
        client.unload_extension(f'cogs.{extension}')
    except:
        pass
    client.load_extension(f'cogs.{extension}')
    await ctx.send("effectué")

for x in os.listdir('./cogs'):
    if x.endswith('.py'):
        client.load_extension(f'cogs.{x[:-3]}')


client.run( data.discord_tokken() )
