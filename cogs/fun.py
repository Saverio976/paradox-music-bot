import discord
from discord.ext import commands
from assets.module import gif
from random import choice

client = commands.Bot(command_prefix = commands.when_mentioned_or('!'))

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def hug(self, ctx, someone:discord.Member):
        embed_hug =   discord.Embed(title="hug",
                                    description = f"{ctx.author} fait un calin à {someone}",
                                    colour = 0xFF0000,
                                    timestamp = ctx.message.created_at)
        embed_hug.set_image(url = await gif.random_hug())
        embed_hug.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed_hug)

    @commands.command()
    async def cookie(self, ctx, someone:discord.Member):
        embed_cookie =  discord.Embed(title="cookie",
                                      description = f"{ctx.author} donne un cookie à {someone}",
                                      colour = 0xFF0000,
                                      timestamp = ctx.message.created_at)
        embed_cookie.set_image(url = await gif.random_cooki())
        embed_cookie.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed_cookie)

    @commands.command()
    async def punish(self, ctx, someone:discord.Member):
        embed_punish =  discord.Embed(title="punishment",
                                      description = f"{ctx.author} puni {someone}",
                                      colour = 0xFF0000,
                                      timestamp = ctx.message.created_at)
        embed_punish.set_image(url = await gif.random_punish())
        embed_punish.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed_punish)

    @commands.command()
    async def award(self, ctx, someone:discord.Member):
        embed_award =  discord.Embed(title="award",
                                      description = f"{ctx.author} récompense {someone}",
                                      colour = 0xFF0000,
                                      timestamp = ctx.message.created_at)
        embed_award.set_image(url = await gif.random_award())
        embed_award.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed_award)

    @commands.command(aliases = ["8ball", "sure"])
    async def _8ball(self, ctx, *, question):
        answer =   ['It is certain.', 'it is decidedly so.', 'Witout a doubt.', 'Yes, definitely.', 'You may rely on it.',
                    'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
                    'Reply hazy, try later.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.',
                    'Concentrate and ask again.', "Don't count on it.", 'My reply is no.', 'My sources say no.',
                    'Outlook not so good.', 'Very doubtful.', "C'est certain", "C'est décidément ainsi",
                    "Ainsi soit-il", "C'est ainsi", "Sans aucun doute", "Oui, définitivement",
                    "Vous devriez vous faire confiance", "Comme je le vois, oui", "C'est tout comme",
                    "Répétez la question", "Demandez plus tard", "C'est mieux de na pas le dire maintenant",
                    "Je ne peux le dire maintenant", "Ne comptez pas dessus", "Mes sources disent non",
                    "Il y a vraiment des doutes"]
        await ctx.send(f'```Question: {question}```\nAnswer: {choice(answer)}')

def setup(client):
    client.add_cog(Fun(client))
