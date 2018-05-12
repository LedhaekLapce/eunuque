import sys
import os

#from PIL import Image, ImageDraw, ImageFont
#import matplotlib.pyplot as plt
#import matplotlib.font_manager as fm
#import textwrap

from discord.ext import commands
from sous.secret import token

from yaml import load, dump

import random as rd


import urllib.request

opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0')]
urllib.request.install_opener(opener)




print(token)

with open('./listgif.yaml') as f :
    listegif = load(f)





description = """
Gnééééééééééééééééééééééééééééééééééééééééééééééééé.
"""


bot = commands.Bot(command_prefix="enu ", description=description)



@bot.command(pass_context=True)
async def gif(ctx, *, message) :
    await bot.type()
    if message=='list' :
        print(listegif)
        gne="__Liste des gifs disponibles :__"
        for i in sorted(listegif) :
            gne+='\n'+i
        await bot.say(gne)  
    elif message in listegif :
        await bot.upload('./gifs/'+message+'.gif')
    else :
        await bot.say("Ce gif n'existe pas ! (encore...)")


@bot.command(pass_context=True,help="Tapez :addgif help pour plus d'info.")
async def addgif(ctx, message) :
    if message in listegif :
        await bot.say("Le nom `"+message+"` est déjà pris.")
    elif message=='list' :
        await bot.say("Are you kidding me ?")
    elif message=='help' :
        await bot.upload('aideaddgif.png')
    else :
        list_url = [i['url'] for i in ctx.message.embeds] + [i['proxy_url'] for i in ctx.message.attachments]
        for i, url in enumerate(list_url):
            urllib.request.urlretrieve(url, "./gifs/"+message+".gif")
        listegif.append(message)
        with open('./listgif.yaml','w') as f :
            dump(listegif,f)


PACH=['https://youtu.be/R2RpCeEJDZQ','https://youtu.be/nuvUxlvvh6o','https://youtu.be/tDVUnnCrCw8','https://youtu.be/C6YfURMQaXw','https://youtu.be/bPzG2SHXXng','https://youtu.be/l6fuXh1MdRU','https://youtu.be/mCLry9GIxcw','https://youtu.be/Q4JQSnDtrw4','https://youtu.be/OhZNozUMtk8','https://youtu.be/0Pce0g310Ec','https://youtu.be/haoIGyhZoo8','https://youtu.be/ZHwYr_1yGO4',"Désolé mais @Pigiste#1100 n'a pas sorti de vidéo depuis février..."]

@bot.command()
async def unpeudePACH() :
    await bot.say(rd.choice(PACH))



@bot.command(pass_context=True,hidden=True)
async def test(ctx, *, message):
    if ctx.message.author.bot:
        return
    await bot.say(message)

@bot.command(pass_context=True,description='Fonction test',hidden=True)
async def test2(ctx, *, message) :
    await bot.type()
    await bot.say(ctx.message.author.id)



@bot.listen('on_ready')
async def login():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')



bot.run(token)














