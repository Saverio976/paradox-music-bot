import subprocess
from asyncio import get_event_loop
from concurrent.futures import ThreadPoolExecutor

async def info(url_info, numero = 0):
    def get_info():
        if url_info.startswith('http'):
            command = ['youtube-dl','-x','--audio-format', 'mp3', url_info,'-e', '--get-thumbnail', '--get-duration', '--no-playlist']
            return subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True).stdout.split('\n')
        else:
            if numero == 0:
                command =['youtube-dl','-x','--audio-format', 'mp3', 'ytsearch:"' + url_info + '"', '-e', '--get-thumbnail', '--get-duration', '-j', '--no-playlist']
            else:
                command = ['youtube-dl','-x','--audio-format', 'mp3', f'ytsearch{numero+1}:"{url_info}"', '--get-title', '--get-thumbnail', '--get-duration', '-j', '--no-playlist']
            info = subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True).stdout.split('\n')
            index_webpage_url = info[ len(info) - 2 ].index('webpage_url')
            compteur_quote_mark = 0
            i = 0
            webpage_url = ''
            while compteur_quote_mark != 3:
                webpage_url += info[ len(info) - 2 ][index_webpage_url + i]
                i += 1
                if webpage_url[-1] == '"':
                    compteur_quote_mark += 1
            webpage_url = webpage_url.split()
            webpage_url = webpage_url[1].strip('"')
            return [ info[ len(info) - 5 ], info[ len(info) - 4 ], info[ len(info) - 3 ], webpage_url, info[ len(info) - 1 ] ]

    loop = get_event_loop()
    info_m = await loop.run_in_executor(ThreadPoolExecutor(), get_info)
    return info_m

async def ytsearch(query):
    def get_urls():
        command = ['youtube-dl','-x','--audio-format', 'mp3', 'ytsearch10:"' + query + '"', '-e', '--get-thumbnail', '--get-duration', '--no-playlist']
        return subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True).stdout
    loop = get_event_loop()
    urls = await loop.run_in_executor(ThreadPoolExecutor(), get_urls)

    r_list = []
    msg = ''
    info = []
    compteur = 0
    for i in urls:
        if i == '\n':
            info.append(msg)
            compteur += 1
            msg = ''
        else:
            msg += i
        if compteur == 3:
            r_list.append(info)
            info = []
            compteur = 0

    return r_list

async def yt_playlist_list_musique(link):
    def get_urls():
        command = ['youtube-dl', link, '-j']
        l_info = subprocess.run(command,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    universal_newlines=True).stdout.split('\n')
        list_link = []
        for info in l_info:
            try:
                index_webpage_url = info.index('webpage_url')
            except:
                pass
            else:
                compteur_quote_mark = 0
                i = 0
                webpage_url = ''
                while compteur_quote_mark != 3:
                    webpage_url += info[index_webpage_url + i]
                    i += 1
                    if webpage_url[-1] == '"':
                        compteur_quote_mark += 1
                webpage_url = webpage_url.split()
                webpage_url = webpage_url[1].strip('"')
                list_link.append(webpage_url)
        return list_link
    loop = get_event_loop()
    list_link = await loop.run_in_executor(ThreadPoolExecutor(), get_urls)
    return list_link


async def ytdownload(query, num = 0):
    def get_urls():
        if query.startswith('http'):
            command = ['youtube-dl','-x','--audio-format', 'mp3', query,'--get-title', '--get-url', '--get-thumbnail', '--get-duration', '-j', '--no-playlist']
            return subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True).stdout.split('\n')
        else:
            if num == 0:
                command =['youtube-dl','-x','--audio-format', 'mp3', 'ytsearch:"' + query + '"', '--get-title', '--get-url', '--get-thumbnail', '-j', '--no-playlist']
            else:
                command = ['youtube-dl','-x','--audio-format', 'mp3', f'ytsearch{num+1}:"{query}"', '--get-title', '--get_url', '--get-thumbnail', '-j', '--no-playlist']
            info = subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True).stdout.split('\n')
            index_webpage_url = info[ len(info) - 2 ].index('webpage_url')
            compteur_quote_mark = 0
            i = 0
            webpage_url = ''
            while compteur_quote_mark != 3:
                webpage_url += info[ len(info) - 2 ][index_webpage_url + i]
                i += 1
                if webpage_url[-1] == '"':
                    compteur_quote_mark += 1
            webpage_url = webpage_url.split()
            webpage_url = webpage_url[1].strip('"')
            # title , link, thumbnail, webpage_url
            return [info[ len(info) - 5 ], info[ len(info) - 4 ], info[ len(info) - 3], webpage_url]
    loop = get_event_loop()
    r_list = await loop.run_in_executor(ThreadPoolExecutor(), get_urls)


    return r_list
