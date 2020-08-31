import discord
from asyncio import get_event_loop

from assets.module import data
from discord.ext import commands
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

client = commands.Bot(command_prefix = commands.when_mentioned_or('!'))

class Event(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('ReAdY')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.type == discord.ChannelType.private:
            if message.author.id not in [710407264070139944, 425965177616334849]:
                for guild in self.client.guilds:
                    for member in guild.members:
                        if member.id == 425965177616334849:
                            saverio = member

                await saverio.send(f"Auteur(e) : {message.author}")
                await saverio.send(f"id : {message.author.id}")
                await saverio.send(f"{message.content}")
                for attachment in message.attachments:
                    await saverio.send(file = discord.File(attachment.to_file()))


    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.channels, name='départ-arrivée')
        await ctx.send(file=discord.File('./images/welcome.jpg'))
        await channel.send(f"Salut à toi, oui toi {member.mention}")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        dictReactionEvent = data.dictReactionEvent()

        guild = self.client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        message_id = payload.message_id

        if payload.emoji.is_custom_emoji():
            emoji = payload.emoji.id
        else:
            emoji = str(payload.emoji)

        if message_id in dictReactionEvent.keys():
            if emoji in dictReactionEvent[message_id].keys():
                role = guild.get_role(dictReactionEvent[message_id][emoji])

                await member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        dictReactionEvent = data.dictReactionEvent()

        guild = self.client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)
        message_id = payload.message_id

        if payload.emoji.is_custom_emoji():
            emoji = payload.emoji.id
        else:
            emoji = str(payload.emoji)

        if message_id in dictReactionEvent.keys():
            if emoji in dictReactionEvent[message_id].keys():
                role = guild.get_role(dictReactionEvent[message_id][emoji])

                await member.remove_roles(role)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("CommandNotFound")
        if isinstance(error, commands.MissingRole):
            await ctx.send("role is missing to run this command : " + str(error.missing_role))
        else:
            def write_logs():
                with open("./assets/document/bot_logs.txt", "a") as file:
                    file.write(f"\ndate : {datetime.now()} | message : {ctx.message.content} | erreur : {error}")
            loop = get_event_loop()
            try:
                exe = await loop.run_in_executor(ThreadPoolExecutor(), write_logs())
            except TypeError:
                pass
            await ctx.send(f'{error}')

def setup(client):
    client.add_cog(Event(client))
