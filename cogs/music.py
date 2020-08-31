import discord
from discord.ext import commands

from asyncio import get_event_loop, sleep
from concurrent.futures import ThreadPoolExecutor

import pymongo, aiodns

import subprocess
from assets.module import CobraMusic, data, utils

from random import randint

client = commands.Bot(command_prefix = commands.when_mentioned_or('!'))

class Music(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.CompteurMusique = 0
        self.Attente = []
        self.ctx1 = None
        self.muse = ''
        self.DictInfoMusic = {}

    @commands.command(aliases = ['p'])
    async def playL(self, ctx, url):
        '''joue une musique ou la met dans la fille d'Attente'''
        self.Attente.append(url)
        self.DictInfoMusic[url] = await utils.info(url)

        await ctx.send(f"``{self.DictInfoMusic[url][0]}`` *ajoutée à la file d'Attente*")

        if self.CompteurMusique == 0:
            self.CompteurMusique += 1
            self.ctx1 = ctx
            await self.musique()
        else:
            self.CompteurMusique += 1
    @commands.command()
    async def playP(self, ctx, playlist):
        '''ajoute les musiques de la playlist dans la file d'Attente'''
        rdbRss = data.rdbRss()
        query = {'id':int(playlist)}

        with pymongo.MongoClient(rdbRss) as cluster:
            db = cluster['ParadoxMusicBot']
            dtab = db['Playlist']
            x = dtab.find_one(query)['urls']

        for i in x:
            self.DictInfoMusic[i] = await utils.info(i)
            self.Attente.append(i)
            await ctx.send(f"``{self.DictInfoMusic[i][0]}`` *ajoutée à la file d'Attente*")

        if self.CompteurMusique == 0:
            self.CompteurMusique += 1
            self.ctx1 = ctx
            await self.musique()
        else:
            self.CompteurMusique += 1
    @commands.command()
    async def playS(self, ctx, query, num = "0"):
        '''ajouter des musiques par recherche de mots clefs
        Attention, les mots clefs doivent être mis entre guillemet ("ma recherche sur youtube")'''
        try:
            num = int(num)
        except:
            await ctx.send("veuillez bien verifier si vos mots clefs sont entre guillemets")
            return
        if num > 9 or num < 0:
            await ctx.send('numéro choisis trop grand (compris entre 0 et 9)')
            return

        def get_urls():
            command = ['youtube-dl','-x','--audio-format', 'mp3', 'ytsearch10:"' + query + '"', '-g', '--no-playlist']
            return subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True).stdout.split('\n')
        loop = get_event_loop()
        urls = await loop.run_in_executor(ThreadPoolExecutor(), get_urls)

        self.DictInfoMusic[urls[num]] = await utils.info(query, num)
        self.Attente.append(urls[num])
        await ctx.send(f"``{self.DictInfoMusic[urls[num]][0]}`` *ajoutée à la file d'Attente*")

        if self.CompteurMusique == 0:
            self.CompteurMusique += 1
            self.ctx1 = ctx
            await self.musique()
        else:
            self.CompteurMusique += 1


    @commands.command()
    async def search(self, ctx, *, query):
        r_list = utils.ytsearch()

        await ctx.send(f"voici la recherche sur youtube avec le(s) mot(s) clef(s) ``{query}`` : ")
        for i in range(len(r_list)):
            if len(r_list[i]) >= 3:
                emb = discord.Embed(title=f"{i} : {r_list[i][0]}", description=f"temps : {r_list[i][2]}", color=0xd92626)
                emb.set_thumbnail(url=r_list[i][1])
                await ctx.send(embed = emb)
                await sleep(0.9)


    @commands.command(name='now playing',aliases=['np','now'])
    async def now(self, ctx):
        '''Pour savoir qu'est-ce qui est joué comme musique.'''
        info = self.DictInfoMusic[self.muse]

        if len(info) >= 3:
            if len(info) == 5:
                emb = discord.Embed(title = info[0], url = info[3], description=f"temps : {info[2]}", color=0xd92626)
            else:
                emb = discord.Embed(title = info[0], url = self.muse, description=f"temps : {info[2]}", color=0xd92626)
            emb.set_thumbnail(url=info[1])
            await ctx.send(embed = emb)
        else:
            emb = discord.Embed(title = "unknow", description = self.muse)
            await ctx.send(embed = emb)
    @commands.command(aliases=['q'])
    async def queue(self, ctx):
        '''Le bot te donnera la liste des prochaines musiques.'''

        await ctx.send("Voici les musiques dans la playlist :")

        if bool(self.muse):
            info = self.DictInfoMusic[self.muse]

            if len(info) >= 3:
                if len(info) == 5:
                    emb = discord.Embed(title = info[0], url = info[3], description=f"temps : {info[2]}", color=0xd92626)
                else:
                    emb = discord.Embed(title = info[0], url = self.muse, description=f"temps : {info[2]}", color=0xd92626)
                emb.set_thumbnail(url=info[1])
                await ctx.send('maintenant :')
                await ctx.send(embed = emb)
            else:
                emb = discord.Embed(title = "unknow", description = self.muse)
                await ctx.send(embed = emb)
            await sleep(1)

        if bool(self.Attente):
            await ctx.send('suivent :')
            for i in range(len(self.Attente)):
                info = self.DictInfoMusic[self.Attente[i]]

                if len(info) >= 3:
                    if len(info) == 5:
                        emb = discord.Embed(title = f"{i+1} : {info[0]}", url = info[3], description=f"temps : {info[2]}", color=0xd92626)
                    else:
                        emb = discord.Embed(title = f"{i+1} : {info[0]}", url = self.muse, description=f"temps : {info[2]}", color=0xd92626)
                    emb.set_thumbnail(url=info[1])
                    await ctx.send(embed = emb)
                else:
                    emb = discord.Embed(title = "unknow", description = self.Attente[i])
                    await ctx.send(embed = emb)
                await sleep(1)


    @commands.command()
    async def shuffle(self, ctx):
        '''pour mettre dans le desordre les musiques'''
        att = self.Attente
        newAtt = []
        while bool(att):
            x = randint(0,len(att)-1)
            url = att[x]
            del att[x]
            newAtt.append(url)
        self.Attente = newAtt
        await ctx.send("Liste d'Attente chamboulée")
    @commands.command(aliases=['s'])
    async def skip(self, ctx):
        '''Pour passer à la musique suivente.'''
        music_client = await CobraMusic.get_client(self.ctx1.message,client)
        await music_client.stop()
    @commands.command()
    async def remove(self, ctx, index):
        try:
            index = int(index)
        except ValueError:
            await ctx.send("envoyez un nombre valide")
            return
        await ctx.send(f"*cette musique ne sera pas jouée* : ``{self.Attente.pop(index)}``")


    @commands.command()
    async def pause(self, ctx):
        '''Mets en pause la musique.'''
        music_client = await CobraMusic.get_client(ctx.message,client)
        if await music_client.is_playing():
            await music_client.pause()
            msg = await ctx.send('music en pause')
            emoji = discord.utils.get(ctx.guild.emojis, id = 710426812878028800)
            await msg.add_reaction(emoji)
        else:
            await ctx.send("La musique est déjà en pause ou il n'y a pas de musique")
    @commands.command()
    async def resume(self, ctx):
        '''Reprends la musique mise en pause.'''
        music_client = await CobraMusic.get_client(ctx.message,client)
        if await music_client.is_paused():
            await music_client.resume()
            msg = await ctx.send('la music redémare !')
            emoji = discord.utils.get(ctx.guild.emojis, id = 710426812878028800)
            await msg.add_reaction(emoji)
        else:
            await ctx.send("La musique n'est pas arrêtée ou il n'y a pas de musique")


    @commands.command(aliases=['dc','leave','l'])
    async def disconnect(self, ctx):
        '''Pour faire déconnecter le bot du channel vocal.'''
        self.CompteurMusique = 0
        self.Attente = []
        self.muse = ''
        music_client = await CobraMusic.get_client(ctx.message,client)
        if await music_client.is_connected():
            await music_client.disconnect()
            msg = await ctx.send('Au revoir !')
            emoji = discord.utils.get(ctx.guild.emojis, id = 710426812878028800)
            await msg.add_reaction(emoji)
    @commands.command()
    async def stop(self, ctx):
        '''Une commande un peu comme disconnect, la différence : il va rester dans le channel.'''
        self.CompteurMusique = 0
        self.Attente = []
        self.muse = ''
        music_client = await CobraMusic.get_client(ctx.message,client)
        await music_client.stop()
        msg = await ctx.send('music arrêté !')
        emoji = discord.utils.get(ctx.guild.emojis, id = 710426812878028800)
        await msg.add_reaction(emoji)


    @commands.command()
    async def addP(self, ctx, *, name):
        '''permet de créer une nouvelle playlist'''
        rdbRss = data.rdbRss()

        with pymongo.MongoClient(rdbRss) as cluster:
            db = cluster['ParadoxMusicBot']
            dtab = db['Playlist']
            x = dtab.find()
            cpt=0
            for i in x:
                cpt += 1
            p = {
                'id' : cpt + 1,
                'name' : name,
                'urls' : []
            }
            x = dtab.insert_one(p)
        await ctx.send('Action réalisée')
    @commands.command()
    async def removeP(self, ctx, playlist):
        '''pour supprimer une playlist'''
        rdbRss = data.rdbRss()

        with pymongo.MongoClient(rdbRss) as cluster:
            db = cluster['ParadoxMusicBot']
            dtab = db['Playlist']
            query = {'id':int(playlist)}
            x = dtab.delete_one(query)
            x = dtab.find()
            for i in x:
                query = {'name':i['name']}
                new_val = {"$inc":{"id": -1}}
                dtab.update_one(query,new_val)
        await ctx.send("Playlist supprimée")
    @commands.command()
    async def viewP(self, ctx, mode = "no"):
        '''pour voir les playlist déjà créée et leurs musiques'''
        rdbRss = data.rdbRss()

        with pymongo.MongoClient(rdbRss) as cluster:
            db = cluster['ParadoxMusicBot']
            dtab = db['Playlist']
            if mode == "no":
                x = dtab.find()
                cpt = 0
                for i in x:
                    await ctx.send(f"``{i['name']}`` : ``{i['id']}``")
                    for e in i['urls']:
                        await ctx.send(f'``{e}``')
                        await sleep(1)
                    cpt += 1
                await ctx.send(f"en tout, il y a {cpt} playlist")
            else:
                try:
                    query = {'id': int(mode)}
                except:
                    await ctx.send('Veullez entrer un numéro de playlist')
                    return
                x = dtab.find(query)
                cpt_m = 0
                for i in x:
                    await ctx.send(f"``{i['name']}`` : ``{i['id']}``")
                    for e in i['urls']:
                        await ctx.send(f'{e}')
                        await sleep(1)
                        cpt_m += 1
                await ctx.send(f"en tout, il y a {cpt_m} musique(s) dans la playlist")

    @commands.command()
    async def addM(self, ctx, playlist, url):
        '''permet d'ajouter de la musique dans une playlist'''
        rdbRss = data.rdbRss()
        with pymongo.MongoClient(rdbRss) as cluster:
            db = cluster['ParadoxMusicBot']
            dtab = db['Playlist']
            query = {'id' : int(playlist)}
            new_val = {'$addToSet':{'urls':url}}
            x = dtab.update_many(query,new_val)
        if x.modified_count == 0:
            await ctx.send(f"il n'y a pas de playlist correspondant au numéro {playlist}" )
        else:
            await ctx.send("La playlist a été modifiée")
    @commands.command()
    async def removeM(self, ctx, playlist, url):
        '''permet d'enlever de la musique dans une playlist'''
        rdbRss = data.rdbRss()

        with pymongo.MongoClient(rdbRss) as cluster:
            db = cluster['ParadoxMusicBot']
            dtab = db['Playlist']
            query = {'id' : int(playlist)}
            x = dtab.find_one(query)
            Lurls = x['urls']
            nb = Lurls.index(url)
            del Lurls[nb]
            new_val = {'$set': {'urls' : Lurls }}
            d = dtab.update_one(query,new_val)
        await ctx.send('La playlist a bien été modifiée')


    @commands.command()
    async def downloadyt(self, ctx, query, number = "0"):
        try:
            number = int(number)
        except:
            await ctx.send("veuillez bien verifier si vos mots clefs sont entre guillemets")
            return
        if number > 9 or number < 0:
            await ctx.send('numéro choisis trop grand (compris entre 0 et 9)')
            return

        musique = await utils.ytdownload(query, number)

        emb = discord.Embed(title = f"{musique[0]}", url = f"{musique[3]}")
        emb.set_thumbnail(url = f"{musique[2]}")
        emb.add_field(name = "download", value = f"{musique[1]}")
        await ctx.send(embed = emb)



    async def musique(self):
        music_client = await CobraMusic.get_client(self.ctx1.message,client)
        while bool(self.Attente):
            self.muse = self.Attente[0]
            del self.Attente[0]
            is_ok = await music_client.play(self.muse)

            if is_ok:
                info = self.DictInfoMusic[self.muse]
                if len(info) > 3:
                    if len(info) == 5:
                        embed = discord.Embed(title = info[0], url = info[3], color=0xab3636)
                    else:
                        embed = discord.Embed(title = info[0], url = self.muse, color=0xab3636)
                    embed.set_thumbnail(url = info[1])
                    embed.add_field(name = "Now Playing", value=f"temps : {info[2]}")
                    await self.ctx1.send(embed=embed)
                else:
                    embed = discord.Embed(title="now playing", url = self.muse, color=0xab3636)
                    embed.add_field(name="unknow", value = self.muse)
                    await self.ctx1.send(embed=embed)
            else:
                await self.ctx1.send("une erreur s'est produite lors de la lecture de cette musique : " + str(self.muse))

            while await music_client.is_playing() or await music_client.is_paused():
                await sleep(2)
        self.CompteurMusique = 0
        self.muse = ''
        self.DictInfoMusic = {}
        await music_client.disconnect()


def setup(client):
    client.add_cog(Music(client))
