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
import asyncio
import discord
import aiohttp
import typing



bot = discord.Bot()

@bot.event
async def on_ready():
    print('The Public Bot is online')


@bot.command(description="RPS vs the Bot")
async def rps(ctx):
    choices = ["🤜", "✋", "✌️"]
    computer_answer = random.choice(choices)

    def check(reaction, user):
        return user == ctx.author and reaction.emoji in choices

    pickChoiceEmbed = discord.Embed(title="Make your choice!", description=f"**Rock! Paper! Scissors!**", color=0xFF5733)
    pickChoiceEmbed.set_footer(text="Choose in 60 Seconds or you lose!")
    pickChoiceEmbed.add_field(name="🤜", value="Rock")
    pickChoiceEmbed.add_field(name="✋", value="Paper")
    pickChoiceEmbed.add_field(name="✌️", value="Scissors")
    message = await ctx.send(embed=pickChoiceEmbed)
    await message.add_reaction("🤜")
    await message.add_reaction("✋")
    await message.add_reaction("✌️")

    try:
        reaction, user = await bot.wait_for("reaction_add", check=check, timeout=60.0)
    except asyncio.TimeoutError:
        await ctx.send("You ran out of time... You lose!")
        return
    answer = reaction.emoji
    if computer_answer == answer:
        await ctx.send(f"Tie! We both picked **{answer}**")
    if computer_answer == "🤜":
        if answer == "✋":
            await ctx.send(f"You win! I picked {computer_answer} and you picked {answer}")
        elif answer == "✌️":
            await ctx.send(f"I win! I picked {computer_answer} and you picked {answer}")
    elif computer_answer == "✋":
        if answer == "🤜":
            await ctx.send(f"I win! I picked {computer_answer} and you picked {answer}")
        elif answer == "✌️":
            await ctx.send(f"You win! I picked {computer_answer} and you picked {answer}")
    elif computer_answer == "✌️":
        if answer == "🤜":
            await ctx.send(f"You win! I picked {computer_answer} and you picked {answer}")
        elif answer == "✋":
            await ctx.send(f"I win! I picked {computer_answer} and you picked {answer}") 
    
#RPS a person of your choice
@bot.command(description="Use this command to face someone in Rock Paper Scissors!")
async def rps_someone(ctx, member: discord.Member):
    question_embed = discord.Embed(title="Would you like to play?", description=f"{ctx.author.mention} has challenged you to RPS. Do you accept?",color=0xD75BF4)
    question_msg = await ctx.send(member.mention, embed=question_embed)
    await question_msg.add_reaction("✅")
    await question_msg.add_reaction("❌")

    def check(reaction, user):
        return user == member and str(reaction.emoji) in ["✅", "❌"]

    try:
        reaction, user = await bot.wait_for("reaction_add", check=check, timeout=60.0)
    except asyncio.TimeoutError:
        await ctx.send("Nobody made a choice in 60 Seconds... Nobody Wins!")
        return
    if str(reaction.emoji) == "❌":
        await ctx.send(f"{member.mention} doesn't want to play.")
        return
    elif str(reaction.emoji) == "✅":
        choices = ["🤜", "✋", "✌️"]
        player1 = (ctx.author, None)
        player2 = (member, None)
        def check(reaction, user):
            return user in (player1[0], player2[0]) and reaction.emoji in choices

        pickChoiceEmbed = discord.Embed(title="Make your choice!", description=f"**Rock! Paper! Scissors!**", color=0xFF5733)
        pickChoiceEmbed.set_footer(text="Choose in 60 Seconds or you lose!")

        message = await ctx.send(embed=pickChoiceEmbed)
        await message.add_reaction("🤜")
        await message.add_reaction("✋")
        await message.add_reaction("✌️")
        try:
            while player1[1] is None or player2[1] is None:
                reaction, user = await bot.wait_for("reaction_add", check=check, timeout=60)
                if user == player1[0]:
                    player1 = (player1[0], reaction.emoji)
                    await ctx.send(f"{player1[0].mention} has chosen an option!")
                else:
                    player2 = (player2[0], reaction.emoji)
                    await ctx.send(f"{player2[0].mention} has chosen an option!")
        except asyncio.TimeoutError:
            await ctx.send("Nobody made a choice in 60 Seconds... Nobody Wins!")
            return
        if player1[1] == player2[1]:
            await ctx.send(f"Tie! Both {player1[0].mention} and {player2[0].mention} picked **{player1[1]}**")
        elif player1[1] == "🤜" and player2[1] == "✋":
            await ctx.send(f"{player1[0].mention} wins! They picked {player1[1]} and {player2[0].mention} picked **{player1[1]}**")
        else:
            if player1 is None:
                player1 = (user, reaction.emoji)
                await ctx.send(f"{user.mention} has chosen {reaction.emoji}")
            elif player2 is None:
                player2 = (user, reaction.emoji)
                await ctx.send(f"{user.mention} has chosen {reaction.emoji}")
            if player1[1] and player2[1]: #check if both players have made their choice
                if player1[1] == player2[1]:
                    await ctx.send("It's a tie!")
                elif (player1[1] == "🤜" and player2[1] == "✌️") or (player1[1] == "✋" and player2[1] == "🤜") or (player1[1] == "✌️" and player2[1] == "✋"):
                    await ctx.send(f"{player1[0].mention} wins! They picked {player1[1]} and {player2[0].mention} picked {player2[1]}")
                else:
                    await ctx.send(f"{player2[0].mention} wins! They picked {player2[1]} and {player1[0].mention} picked {player1[1]}")
                return




              

bot.run("token")
