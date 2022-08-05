import os
from dotenv import load_dotenv
import discord
import time

def configure():
  load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
  print(f'{client.user} is online!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!meowtimer'):
    input = message.content.split()
    await message.channel.send("meow timer starting now!")
    try:
      time.sleep(float(input[1]))
      await message.channel.send("meow!")
    except:
      time.sleep(float(3))
      await message.channel.send("meow!")
    return
      
  if message.content.startswith('!meow'):
    input = message.content.split()
    amt = int(input[1])
    if amt <= 50 and amt > 0:
      await message.channel.send("meow"*amt)
    else:
      await message.channel.send("too many meows... shutting down")
    return
  
  if 'meow' in message.content:
    await message.channel.send("meow!")
    return

configure()
client.run(os.environ['meow'])