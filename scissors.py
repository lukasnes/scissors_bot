import discord
import asyncio
import os
from random import choice

client = discord.Client()

@client.event
async def on_ready():
    print(f'Successfully connected! Logged in as {client.user}')

@client.event
async def on_message(self,message):
    if message.author == client.user:
        return
    
    if message.content.startswith('#play'):
        channel = message.channel
        await channel.send("You're not ready for this jelly.")

        def choose(m):
            if m.content == 'rock':
                return m.author == message.author and m.content == 'rock'
            elif m.content == 'paper':
                return m.author == message.author and m.content == 'paper'
            elif m.content == 'scissors':
                return m.author == message.author and m.content == 'scissors'

        bot_choice = choice(['rock','paper','scissors'])

        def lose_text(choice):
            text = [
                f"I can't believe it! And here that merchant told me this was special {choice}",
                f"Wow, seriously? I spent hours trying to find this here {choice}",
                f"Are you sure ya ain't cheatin'? You strike me as the cheatin' type.",
                f"Oho! We got a smart one. Or at least, they think they are. Goin' 'round destroyin' my {choice}",
                f"Alright, now you're just playin' plain dirty."
            ]
            loser = choice(text)
            return loser

        def victory_text(player_choice,bot_choice):
            text = [
                f"Hahaaaa! I knew I bet on the right {bot_choice}!",
                f"Aww, don't cry. Not everyone can have a {bot_choice} like me.",
                f"Alright, I won! Now go on, 'git!",
                f"Well, with a {player_choice} like that, it's not a wonder my {bot_choice} won."
                f"Are you even tryin'? Who picks {player_choice}? Well, I certainly do not, cuz I picked {bot_choice}"
            ]
            winner = choice(text)
            return winner

        try:
            player_choice = await self.wait_for('message',check=choose,timeout=10.0)
        except asyncio.TimeoutError:
            return await message.channel.send("What's 'a matter? You chicken?")
        if player_choice == bot_choice:
            return await message.channel.send(f"What in tarnation? I picked {bot_choice} too! Ya cheatin' or sumthin'?")
        elif player_choice == "scissors" and bot_choice == "paper":
            return await message.channel.send(lose_text(bot_choice))
        elif player_choice == "paper" and bot_choice == "rock":
            return await message.channel.send(lose_text(bot_choice))
        elif player_choice == "rock" and bot_choice == "scissors":
            return await message.channel.send(lose_text(bot_choice))
        else:
            return await message.channel.send(victory_text(player_choice,bot_choice))
        

client.run(os.environ['DISCORD_TOKEN'])