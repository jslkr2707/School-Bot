import discord
import datetime
import dataframe_image
from discord.ext import tasks, commands
from os.path import exists
import numpy as np

#custom modules
from timetable import *
import fileHandler as fh
import spreadHandler as sh

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all(), status=discord.Status.online)
today = datetime.datetime.today(); date = today.isoformat().replace("-", "")

@bot.event
async def on_ready():
    print("Connection Successful")

@bot.command()
async def register(ctx, school):
    if sh.userValid(ctx.author.id):
        await ctx.reply('이미 등록된 사용자입니다!')
    else:
        if fh.schoolValid(school):
            fh.register(ctx.author.id, school)
            await ctx.reply('성공적으로 학교가 등록되었습니다!')
        else:
            await ctx.reply('등록에 실패했습니다. 학교 이름이 정확한지 확인해주세요.')

@bot.command()
async def info(ctx):
    if (sh.userValid(ctx.author.id)):
        school = fh.getSchool(ctx.author.id)
        await ctx.reply('학교명: %s'%school)
    else:
        await ctx.reply('등록되지 않은 사용자입니다!')
        
bot.run("asdf") #token reset, don't even try
