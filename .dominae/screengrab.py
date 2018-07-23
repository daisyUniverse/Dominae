#Screengrabbot by Ewi OwO

from discord.ext.commands import Bot
from discord.ext import commands
from datetime import datetime
from os import path
import subprocess
import discord
import asyncio

client = commands.Bot(command_prefix='>')
cwd = path.abspath(path.curdir + "dominae")

@client.event
async def on_ready():
    print ("Bot Core Ready \n")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.author.bot: return

    channel = message.channel
    author  = message.author
    
    if message.content.startswith('sfull'):

        subprocess.check_output(cwd + "/sfull.sh")
        await channel.send(file=discord.File(cwd + "/sfull.png"))

        print ("Full Screenshot Uploaded ")
        print ('by {} at {} \n'.format(author, str(datetime.now())))

    if message.content.startswith('swindow'):

        subprocess.check_output(cwd + "/swindow.sh")
        await channel.send(file=discord.File(cwd + "/swindow.png"))

        print ("Window Screenshot Uploaded")
        print ('by {} at {} \n'.format(author, str(datetime.now())))

    if message.content.startswith('sselect'):

        subprocess.check_output(cwd + "/sselect.sh")
        await channel.send(file=discord.File(cwd + "/sselect.png"))

        print ("Rectangle Select Screenshot Uploaded")
        print ('by {} at {} \n'.format(author, str(datetime.now())))

    if message.content.startswith('sweb'):

        await channel.send("... Snap!")
        subprocess.check_output(cwd + "/sweb.sh")
        await channel.send(file=discord.File(cwd + "/sweb.png"))
        await channel.send("Now THAT'S going in my Cringe Compilation!")

        print ("Webshot Uploaded")
        print ('by {} at {} \n'.format(author, str(datetime.now())))

    if message.content.startswith('cls'):

        await channel.send(file=discord.File(cwd + "/Blank.png"))
        await channel.send(file=discord.File(cwd + "/Blank.png"))
        await channel.send(file=discord.File(cwd + "/Blank.png"))
        await channel.send(file=discord.File(cwd + "/Blank.png"))

        print ("Chat Cleared")
        print ('by {} at {} \n'.format(author, str(datetime.now())))

    if message.content.startswith('smov'):

        await channel.send("Recording...Please wait 10s")
        subprocess.check_output(cwd + "/smov.sh")
        await channel.send(file=discord.File(cwd + "/smov.webm"))

        print ("Webm Uploaded")
        print ('by {} at {} \n'.format(author, str(datetime.now())))

    if message.content.startswith('screenfetch'):

        subprocess.check_output(cwd + "/screenfetch.sh")
        await channel.send(file=discord.File(cwd + "/screenfetch.png"))

        print ("Screenfetch Uploaded")
        print ('by {} at {} \n'.format(author, str(datetime.now())))

    if '-ass' in message.content:

        ftfy = message.content.replace( "-ass " , " ass-" )
        await channel.send("\n Fixed that for you : \n" + '```' + "{}".format(author)[:-5] + ": " + ftfy + ' ```')
        await channel.send(file=discord.File(cwd + "/hyphen.jpg"))

        print ("Sweet-Ass Uploaded")
        print ('by {} at {} \n'.format(author, str(datetime.now())))

    if message.content.startswith('ssay'):

        f = open(cwd + '/ssay.txt','w')
        f.write(message.content.replace("ssay ",""))
        f.close()

        subprocess.check_output(cwd + "/ssay.sh")
        await channel.send(file=discord.File(cwd + '/ssay.png'))

        print ("Phrase Uploaded")
        print ("'" + message.content.replace("ssay ","") + "'")
        print ('by {} at {} \n'.format(author, str(datetime.now())))

    if message.content.startswith('svox'):

        voxs = message.content.replace("svox ","")
        voxfn = voxs.replace(" ",".wav \n") + ".wav"
        voxfn += " svox.wav\n"
        f = open(cwd + '/VOX/voxfn.txt','w')
        f.write(voxfn)
        f.close()

        subprocess.check_output(cwd + "/VOX/svox.sh")
        await channel.send(file=discord.File(cwd + '/VOX/svox.wav'))

        print ("Black Mesa Resarch Facility Notified")
        print ("'" + message.content.replace("svox ","") + "'")
        print ('by {} at {} \n'.format(author, str(datetime.now())))

    if message.content.startswith('ssub'):

        f = open(cwd + '/ssub.txt','w')
        f.write(message.content.replace("ssub ",""))
        f.close()

        subprocess.check_output(cwd + "/ssub.sh")
        await channel.send(file=discord.File(cwd + '/ssub.png'))

        print ("Subtitles Uploaded")
        print ("'" + message.content.replace("ssub ","") + "'")
        print ('by {} at {} \n'.format(author, str(datetime.now())))

    if message.content.startswith('help svox'):

        await channel.send("Here are the current VOX keywords.")
        await channel.send(file=discord.File(cwd + "/svox.png"))

        print ("Vox Keywords Shown")
        print ('by {} at {} \n'.format(author, str(datetime.now())))

client.run("TOKEN")
