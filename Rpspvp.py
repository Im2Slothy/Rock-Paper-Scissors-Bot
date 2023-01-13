#THIS REQUIRES PY CORD TO WORK! IF YOU DON'T HAVE IT VISIT THIS LINK FOR HELP! https://guide.pycord.dev/installation #
#Bot created by Slothy#4484 <-- Don't remove this if you plan on taking all this for yourself :)#

import discord
import random
import datetime
from datetime import timedelta
import os
import json
import math
from pydoc import describe
import random
from tkinter import Entry
from typing_extensions import Self
import asyncio
import discord
import aiohttp
import typing
bot = discord.Bot()

@bot.event
async def on_ready():
    print('The Public Bot is online')

class rock(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="", style=discord.ButtonStyle.primary, emoji="🤜") # Create a button with the label "🤜 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked the button!")

class paper(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="", style=discord.ButtonStyle.primary, emoji="✋") # Create a button with the label "🤜 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked the button!")

class scissors(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="", style=discord.ButtonStyle.primary, emoji="✌️") # Create a button with the label "🤜 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked the button!")


# Start of Basic Random Commands to Add to your server #

#Bot's ping command#
@bot.command(description="Sends the bot's latency.") # this decorator makes a slash command
async def ping(ctx): # a slash command will be created with the name "ping"
    embed = discord.Embed(title='My ping!', description=f"**Pong! {round(bot.latency * 1000)}ms**", color=0xFF5733)
    await ctx.respond(embed=embed)























    
#RPS a person of your choice
@bot.command(description="Use this command to face someone in Rock Paper Scissors!")
async def rps_someone(ctx, member: discord.Member)
    embedQuestion = discord.Embed(title="Would you like to play?", description=f"{ctx.author.mention} has challenged you to RPS. Do you accept?",color=0xD75BF4)
              
