import discord
import datetime
from discord.ext import tasks, commands

from meal import *
from timetable import *
from Prefix import *
from event import *

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all(), status=discord.Status.online)
today = datetime.datetime.today()
date = datetime.date.today().isoformat().replace("-", "")
greetings = "안녕하십니까 단대부고 학섕 여러분 저는 교감입니다.".split()

@bot.event
async def on_ready():
    print("Connection Successful")

@bot.command(name='meal')
async def show_meal(ctx):
    message = combine(addPrefix(greetings)) + combine(addPrefix(meal_list(20221230))) + combine(addPrefix(subjects(20221230))) + combine(addPrefix(event_list(20221230)))
    embed = discord.Embed(title=f'{today.month}월 {today.day}일', description= message, color=discord.Color.random())   
    await ctx.send(embed = embed)

bot.run("MTA1NzU3MjQ2MDI1MTMzNjcxNQ.GLCDd3.zW0DfOE0qjdI9K7pc8_SYGmqf4Tm6BBHvnrM0M")