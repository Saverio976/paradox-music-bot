import discord

import pymongo, dns
import datetime, time
import feedparser

from asyncio import get_event_loop

from assets.module import data

from discord.ext import tasks, commands

from concurrent.futures import ThreadPoolExecutor

client = commands.Bot(command_prefix = commands.when_mentioned_or('!'))

class Tasks(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.check_rss.start()
        self.check_playlist.start()

    @tasks.loop(hours = 1.0)
    async def check_rss(self):
        ghf = (datetime.datetime.utcnow() + datetime.timedelta(hours=2)).hour
        if ghf not in [0,1,2,3,4]:
            rss_data = data.rss_data()
            rdbRss = data.rdbRss()

            with pymongo.MongoClient(rdbRss) as cluster:
                db = cluster['ParadoxMusicBot']
                guild = discord.utils.get(self.client.guilds, name='Sale-a-une-mèche')
                date_day1 = (datetime.datetime.utcnow() + datetime.timedelta(hours=-2)).strftime("%Y%m%d%H%M%S")
                date_day2 = (datetime.datetime.utcnow() + datetime.timedelta(days=-1)).strftime("%Y%m%d")
                for key in rss_data.keys():
                    channel = discord.utils.get(guild.channels, name=key)
                    dinfo = db[key]
                    query = {'date' : {'$regex' : date_day2}}
                    x = dinfo.delete_many(query)
                    for url in rss_data[key]["urls"].keys():
                        compteur = 0
                        NewFeed = feedparser.parse(url)
                        current = NewFeed.entries[compteur]
                        pp = current.published_parsed
                        date_publish = time.strftime("%Y%m%d%H%M%S", pp)
                        l_post = []
                        while date_publish > date_day1:
                            query = {'id' : current.id}
                            rsult = dinfo.find(query)
                            inDb = False
                            for f in rsult:
                                inDb = True
                            if not inDb:
                                l_post.insert(0, current.link)
                                feed = {
                                    'id' : current.id,
                                    'date' : str(date_publish)
                                }
                                dinfo.insert_one(feed)
                            compteur += 1
                            if len(NewFeed.entries) == compteur:
                                date_publish = (datetime.datetime.utcnow() + datetime.timedelta(hours = -3)).strftime("%Y%m%d%H%M%S")
                            else:
                                current = NewFeed.entries[compteur]
                                pp = current.published_parsed
                                date_publish = time.strftime("%Y%m%d%H%M%S", pp)
                        for post in l_post:
                            await channel.send(f'{post}')
                            name = rss_data[key]["urls"][url]
                            channel2 = discord.utils.get(guild.channels, name = name)
                            if channel2 != None:
                                await channel2.send(f'{post}')

    @check_rss.before_loop
    async def before_check_rss(self):
        await self.client.wait_until_ready()


    @tasks.loop(hours = 12.0)
    async def check_playlist(self):
        channels = ['1_best-music-mix',
                    '2_all',
                    '3_music-for-focus',
                    '4_magic-vibes']
        guild = discord.utils.get(self.client.guilds, name='Sale-a-une-mèche')
        with pymongo.MongoClient(data.rdbRss()) as cluster:
            db = cluster['ParadoxMusicBot']
            dtab = db['Playlist']
            x = dtab.find()
            cpt = 0
            cpt_m = 0
            for i in x:
                channel_ctx = discord.utils.get(guild.channels, name = channels[cpt])
                await channel_ctx.purge(limit = 1000)
                for e in i['urls']:
                    await channel_ctx.send(f"{e}")
                    cpt_m += 1
                await channel_ctx.send(f"{cpt_m} musiques dans cette playlist !")
                cpt += 1
                cpt_m = 0

    @check_playlist.before_loop
    async def before_check_playlist(self):
        await self.client.wait_until_ready()

def setup(client):
    client.add_cog(Tasks(client))
