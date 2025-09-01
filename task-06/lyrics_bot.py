import requests #for lyrics

from lrclib import LrcLibAPI#for searching

import musicbrainzngs#for track information


import discord # discord connectivity
from discord.ext import commands#for commands
import logging #for loging files
from dotenv import load_dotenv#enviornment token 
import os

musicbrainzngs.set_useragent("DiscordBot", "1.0", "saharshbaiju@gmail.com")
#discord setup
role_name = "legends"

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log',encoding = 'utf-8',mode = 'w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix = '/',intents = intents)
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


@bot.event

async def on_ready():
    print(f"{bot.user.name} ,....BOOTED SUCCESSFULLY")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.author.name}")
 

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)


#|||||||||||||||||||||||||||||||||||||failed attempts|||||||||||||||||||||||||||||||||||||||||||||||||||||

# @bot.command()
# @commands.has_role('legends')
# async def lyrics(ctx,*,query:str):
#     try:
#         song,artist = query.split("-",1)
#         song = song.strip()
#         print(song)
#         print(artist)
#         results = lrclib.search(track=song, artist=artist)
#         await ctx.send(f'{ctx.author.mention}song is on the way')
#         await ctx.send(f'{ctx.author.mention}{results[0].syncedLyrics}')
#         print(results[0].syncedLyrics)

#     except ValueError:
#         await ctx.send("wrong format, Please use this format: /lyrics <song> - <artist>")



# @bot.command()
# @commands.has_role('legends')
# async def lyrics(ctx, *, query: str):
#     song,artist = query.split("-",1)
#     song = song.strip()
#     artist = artist.strip()

#     url = f"https://lrclib.net/api/get?track_name={song}&artist_name={artist}"
#     res = requests.get(url).json()

#     await ctx.send("lyrics loading ....")
#     await ctx.send(res["plainLyrics"])

    # print("Lyrics:", res["plainLyrics"])

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

@bot.command()
async def lyrics(ctx, *, query: str):
    """
    .
    /lyrics <song> - <artist>  
    Fetches and displays song lyrics. 
    """
    try:
        # split query into song and artist
        if "-" not in query:
            await ctx.send("wrong format, please use this format: /lyrics <song> - <artist>")
            return

        song, artist = query.split("-", 1)
        song = song.strip()
        artist = artist.strip()
        print(song)
        print(artist)

        url = f"https://lrclib.net/api/get?track_name={song}&artist_name={artist}"
        res = requests.get(url).json()

        await ctx.send("Lyrics loading...")

        if "plainLyrics" in res and res["plainLyrics"]:
            lyrics = res["plainLyrics"]

            if len(lyrics) <= 2000:
                await ctx.send(lyrics)
            else:
                with open("lyrics.txt", "w", encoding="utf-8") as f:
                    f.write(lyrics)
                await ctx.send("Lyrics too long, sent as file:", file=discord.File("lyrics.txt"))
        else:
            await ctx.send("No lyrics found.")
    except Exception as e:
        await ctx.send(f"Error: {e}")


@bot.command()
async def track(ctx,*,query:str):
    """
    .
    Gives detailed track information 
    /track <Song> - <Artist>
    """
    try:
        # split query into song and artist
        if "-" not in query:
            await ctx.send("wrong format, please use this format: `/lyrics <song> - <artist>`")
            return

        song, artist = query.split("-", 1)
        song = song.strip()
        artist = artist.strip()
        print(song)
        print(artist)

        result = musicbrainzngs.search_recordings(recording = song, artist = artist)
        track = result["recording-list"][0]
        await ctx.send(f"track of information of {song} loading for {ctx.author.name} ...")

        title = track["title"]
        artist_name = track["artist-credit"][0]["artist"]["name"]
        mbid = track["id"]

        album = track["release-list"][0]["title"] if "release-list" in track else "N/A"
        date = track["release-list"][0].get("date", "N/A") if "release-list" in track else "N/A"

        # Format message
        message = f" Title:{title}\n Artist: {artist_name}\nAlbum:{album}\nRelease Date:{date}\n "

        await ctx.send(message)
    except ValueError:
        pass


@bot.command()
async def search(ctx,*,query:str):
    """
    .
    Enables you to search for a song
    /search <song>
    """
    count = 1
    await ctx.send("Searching .... pls wait")
    try:
        song = query
        song = song.strip()
        api = LrcLibAPI(user_agent="my-app/0.0.1")

        results = api.search_lyrics(track_name=song)

        # Print the results
        if result:
            for result in results:
                await ctx.send(f"{count} ){result.artist_name} - {result.track_name} ({result.album_name})")
                count +=1
        else:
            print('no match found')
    except Exception as e:
        await ctx.send(f"no song found {e}")





bot.run(token,log_handler = handler,log_level = logging.DEBUG)

