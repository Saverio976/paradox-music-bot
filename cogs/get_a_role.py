import discord
from discord.ext import commands

from assets.module import data

client = commands.Bot(command_prefix = commands.when_mentioned_or('!'))

class GetARole(commands.Cog):
    '''categorie qui a servi pour get a role'''

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_role('Co Fondateur')
    async def get_a_role(self, ctx):
        '''permet d'initialiser le channel get-a-role'''
        message =   """liste des différents flux pris en comptes par les différents sites :
                    ```France Info (https://www.francetvinfo.fr/)
                    avec ces categories : [politique,justice,europe,marchés,sciences,senté,cinéma]
                    ```
                    ```BFMTV (https://www.bfmtv.com/)
                    avec ces categories : [international,politques,economie/actualité,internet,logiciel]
                    ```
                    ```le Monde (https://www.lemonde.fr/)
                    avec ces categories : [international,politiques,justice,edication,argent,cinéma,arts,médecine,physique]
                    ```
                    ```le Figaro (https://www.lefigaro.fr/)
                    avec ces categories : [politique,international,santé,bourse,emploi,cinéma,arts-expositions]
                    ```

                    (en ce qui concerne l'afp, il y a quelque problème pour le moment)
                    ```l'AFP (https://www.afp.com/).
                    [Je n'ai pu trier le flux rss de l'afp (déjà le lien je l'ai eu sur ce site . . https://www.dsfc.net/internet/veille/fils-rss-afp-reuters-associated-press/, les informations ne seront pas triées pour l'AFP.
                    ```"""
        await ctx.send(message)

        list_messages, list_emoji = await data.get_a_role_messages()

        for i in range(len(list_messages)):
            message = list_messages[i]
            msg = await ctx.send(message)

            emoji = await self.convert_to_emoji(list_emoji[i], ctx.guild.emojis)

            await msg.add_reaction(emoji)

    async def convert_to_emoji(self, query, emojis):
        if query.startswith(":salameche"):
            return discord.utils.get(emojis, name = query.strip(':'))
        else:
            return query

def setup(client):
    client.add_cog(GetARole(client))
