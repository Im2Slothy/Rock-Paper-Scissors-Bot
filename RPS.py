#Made with ❤ by Slothy#4484 If you have any questions please contact! #


import discord

from discord.ext import commands


import random


intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)

client = commands.Bot(command_prefix = ',', intents = intents)


@client.command()
async def servers(ctx):
        servers = list(client.guilds)
        b=discord.Embed(title=f"How Many Servers We in?",description=f'**Active in {len(servers)} servers!!!**',color=0xff80ed)
        await ctx.send(embed=b)

@client.command(help= 'Use ,rps [Choice] in order to play!\n **Make sure [choice] is in lowercase (rock, paper, scissors)**')
async def rps(ctx,message):
    answer = message.lower()
    choices = ["rock", "paper", "scissors"]
    computer_answer = random.choice(choices)
    if answer not in choices:
        await ctx.send("That is not a vaild option! Please use one of these options: rock, paper, or scissors!")
        return
    else:
        if computer_answer == answer:
            await ctx.send(f"Tie! We both picked **{answer}**")
        if computer_answer == "rock":
            if answer == "paper":
                await ctx.send(f"You win! I picked {computer_answer} and you picked {answer}")
        if computer_answer == "paper":
            if answer == "rock":
                await ctx.send(f"I win! I picked {computer_answer} and you picked {answer}")
        if computer_answer == "scissors":
            if answer == "rock":
                await ctx.send(f"You win! I picked {computer_answer} and you picked {answer}")
        if computer_answer == "rock":
            if answer == "scissors":
                await ctx.send(f"I win! I picked {computer_answer} and you picked {answer}")
        if computer_answer == "paper":
            if answer == "scissors":
                await ctx.send(f"You win! I picked {computer_answer} and you picked {answer}")
        if computer_answer == "scissors":
            if answer == "paper":
                await ctx.send(f"I win! I picked {computer_answer} and you picked {answer}")
        
client.run('TOKEN')
