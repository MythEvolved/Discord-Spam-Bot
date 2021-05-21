import discord
import sys
import asyncio
import random
import os
from config import *

client = discord.Client()
token = sys.argv[1]

@client.event
async def on_ready():
  print("Started Image Spam")
  while not client.is_closed:
    image = random.choice(os.listdir(image_directory))
    print(image)
    await client.send_file(discord.Object(id=Discord_Channel), image_directory + image)
    await asyncio.sleep(time_to_wait) # Pause time between images posted.

client.run(token, bot=False)
