import os
from dotenv import load_dotenv
import discord
import time

def configure():
  load_dotenv()

class MeowBot(discord.Client):
    
    # initializing MeowBot!
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    # MeowBot reports connection status
    async def on_ready(self):
        print(f'{self.user} is online!')
        print(client.guilds)
     
    async def on_message(self, message):
        # ensures bot doesn't respond to itself
        if message.author == self.user:
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
    
        if 'kitten' in str(message.author.roles):
            print(message.content)
            await message.add_reaction('❤️')
            return
        
        

intents = discord.Intents.default()
intents.members = True

client = MeowBot()
configure()
client.run(os.environ['meow'])