import discord
import os
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

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = (str(message.author).split("#"))[0]

    if message.content.startswith('$eng-greeting'):
        await message.channel.send(f'Hello!, {username}')

    if message.content.startswith('$french-greeting'):
        await message.channel.send(f'Salut!, {username}')

    if message.content.startswith('$thai-greeting'):
        await message.channel.send(f'สวัสดี!, {username}')

token = os.getenv("BOT_TOKEN")
client.run(str(token))