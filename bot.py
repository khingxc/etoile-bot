import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv
from pathlib import Path

intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.message_content = True

client = commands.Bot(command_prefix="$", intents=intents)

load_dotenv()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.command(name='greeting')
async def greeting(ctx, arg='eng'):
    if ctx.author == client.user:
        return
    username = (str(ctx.author).split("#"))[0]
    if arg == "french" or arg == "francais" or arg == "français":
        await ctx.send(f"salut!, {username}")
    elif arg == "thai" or arg == "ไทย":
        await ctx.send(f"สวัสดี!, {username}")
    elif arg == "eng":
        await ctx.send(f"hi!, {username}")
    else:
        await ctx.send(f"hi!, {username}")

@client.command(name='mental-support')
async def mental_support(ctx):
    mental_support_list = ["don't worry, I got your back! :)", 
                           "be kind to yourself",
                           "you already did a great job.",
                           "it is alright to not be okay.",
                           "you are amazing. <3",
                           "how are you, really?",
                           "I'm proud of you. :)",
                           "let yourself rest.",
                          ]
    if ctx.author == client.user:
        return
    await ctx.send(random.choice(mental_support_list))
    
# command random food

token = os.getenv("BOT_TOKEN")
client.run(str(token))