#Made with ❤ by Slothy#4484 If you have any questions please contact! #


from discord.ext.commands import Bot
import random

client = Bot("/")

@client.command(help="Play with .rps [your choice]")
async def rps(ctx):
    rpsGame = ['rock', 'paper', 'scissors']
    await ctx.send(f"Rock, paper, or scissors? Choose wisely...")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel and msg.content.lower() in rpsGame

    user_choice = await client.wait_for('message', check=check)

    ai_choice = random.choice(rpsGame)
    if user_choice == 'rock':
        if ai_choice == 'rock':
            await ctx.send(f'Well, that was weird. We tied.\nYour choice: {user_choice}\nMy choice: {ai_choice}')
        elif ai_choice == 'paper':
            await ctx.send(f'Nice try, but I always win!\nYour choice: {user_choice}\nMy choice: {ai_choice}')
        elif ai_choice == 'scissors':
            await ctx.send(f"Aw, you beat me. It won't happen again!\nYour choice: {user_choice}\nMy choice: {ai_choice}")

    elif user_choice == 'paper':
        if ai_choice == 'rock':
            await ctx.send(f'How did you win! I demand a rematch!\nYour choice: {user_choice}\nMy choice: {ai_choice}')
        elif ai_choice == 'paper':
            await ctx.send(f'We just tied. I call a rematch!!\nYour choice: {user_choice}\nMy choice: {ai_choice}')
        elif ai_choice == 'scissors':
            await ctx.send(f"Haha! You lost!\nYour choice: {user_choice}\nMy choice: {ai_choice}")

    elif user_choice == 'scissors':
        if ai_choice == 'rock':
            await ctx.send(f'You just got beat by a rock! Loosah!\nYour choice: {user_choice}\nMy choice: {ai_choice}')
        elif ai_choice == 'paper':
            await ctx.send(f'Bruh. 0_0\nYour choice: {user_choice}\nMy choice: {ai_choice}')
        elif ai_choice == 'scissors':
            await ctx.send(f"It looks like we tied....\nYour choice: {user_choice}\nMy choice: {ai_choice}")
