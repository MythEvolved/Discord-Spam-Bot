import discord
import sys
import asyncio
from config import *

client = discord.Client()
token = sys.argv[1]
spam_text = sys.argv[2]
time_between_messages = sys.argv[3]

@client.event
async def on_ready():
  printf("Started Text Spam")
  while not client.is_closed:
    print(spam_text)
    await client.send_message(discord.Object(id=DiscordChannel), spam_text)
    await asyncio.sleep(time_between_messages) # Pause time between messages in seconds.
    
client.run(token, bot=False)
