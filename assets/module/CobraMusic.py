import discord
import youtube_dl
import asyncio

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}
youtube_dl.utils.bug_reports_message = lambda: ''
ffmpeg_options = {
    'before_options': " -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5 -loglevel quiet",
    'options': '-vn -loglevel quiet'
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
clients = {}  # {guild: MusicClient, ...}

async def get_client(message, client):
    global clients
    if not str(message.guild.id) in clients:
        clients[str(message.guild.id)] = await MusicClient.create(message, client)
    return clients[str(message.guild.id)]

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')


    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False, option=None):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            data = data['entries'][0]
        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **option), data=data)

class MusicClient:
    def __init__(self, message, client):
        self.voice_client = None  # init in classmethod
        self.guild_id = message.guild.id
        self.notif_channel = message.channel
        self.client = client

    @classmethod
    async def create(cls, message, client):
        self = MusicClient(message, client)
        if message.author.voice.channel:
            self.voice_client = await message.author.voice.channel.connect()
            return self
        else:
            raise RuntimeError("Le client n'est pas connecté à un salon vocal !")

    async def play(self, url):
        try:
            player = await YTDLSource.from_url(url, loop=self.client.loop, stream=True, option=ffmpeg_options)
            self.voice_client.play(player)
        except:
            return False
        else:
            return True

    async def disconnect(self):
        await self.voice_client.disconnect()
        try:
            del clients[str(self.guild_id)]
        except:
            pass

    async def pause(self):
        self.voice_client.pause()

    async def resume(self):
        self.voice_client.resume()

    async def stop(self):
        self.voice_client.stop()

    async def is_playing(self):
        return self.voice_client.is_playing()

    async def is_paused(self):
        return self.voice_client.is_paused()

    async def is_connected(self):
        return self.voice_client.is_connected()
