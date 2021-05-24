import asyncio
import datetime
import os
import random

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="C!", description="Spirit Bot. Initialized", case_insensitive=True, intents=intents)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == 'C!help':

        embed = discord.Embed(title="Calculator Bot Help Command!", description="Help Command Via Calculator Bot.")
        embed.add_field(name="Addition", value='```C!add [number 1] [number 2]``` This feature adds the 2 numbers.')
        embed.add_field(name="Subtraction", value='```C!sub [number 1] [number 2]``` This feature subtracts the 2 numbers.')
        embed.add_field(name="Multiplication", value='```C!multiply [number 1] [number 2]``` This feature multipies the 2 numbers.')
        embed.add_field(name="Division", value='```C!divide [number 1] [number 2]``` This feature divides the 2 numbers.')
        embed.set_footer(
            text="Help requested by: " + message.author.display_name + " at " + str(datetime.datetime.utcnow()),
            icon_url=message.author.avatar_url)  # + " " + datetime.datetime.utcnow())
        await message.channel.send(content=None, embed=embed)


    if message.content.startswith('C!add'):
        variables = message.content.strip().split(' ')
        num1 = int(variables[1])
        num2 = int(variables[2])
        await message.add_reaction(":Addition: 846427770607108126")
        await message.channel.send(f"{num1 + num2} is the answer to your question")


    if message.content.startswith('C!multiply'):
        variables = message.content.strip().split(' ')
        num1 = int(variables[1])
        num2 = int(variables[2])
        await message.add_reaction(":Multiply: 846428760681218050")
        await message.channel.send(f"{num1 * num2} is the answer to your question")

    if message.content.startswith('C!divide'):
        variables = message.content.strip().split(' ')
        num1 = int(variables[1])
        num2 = int(variables[2])
        await message.add_reaction(":Division: 846428604778414180")
        await message.channel.send(f"{num1 / num2} is the answer to your question")

    if message.content.startswith('C!sub'):
        variables = message.content.strip().split(' ')
        num1 = int(variables[1])
        num2 = int(variables[2])
        await message.add_reaction(":Subtraction: 846427931672969216")
        await message.channel.send(f"{num1 - num2} is the answer to your question")


async def ch_pr():
    await bot.wait_until_ready()

    statuses = ["C!Help", "Prefix: C!", f" The bot is residented in {len(bot.guilds)} servers", "C!add", "C!sub", "C!multiply", "C!divide"]

    while not bot.is_closed():

        status = random.choice(statuses)

        await bot.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(2)

bot.loop.create_task(ch_pr())


bot.run(TOKEN)
