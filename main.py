import discord  
from simsimi import simsimi
from dotenv import load_dotenv
import os

load_dotenv()
channel_name = os.getenv("channel_name")
client = discord.Client()
token = os.getenv("token")

@client.event
async def on_message(msg):
  channel = ["simsimi"] # Enter the channel name for the bot to respond, create a channel in your server with this name
  
  message = msg.content.lower() # Save the message typed by the user by Discord
  
  if msg.author.bot:
    '''
    If the message is from a bot, it will not reply
    '''
    return
  
  if msg.channel.name in channel:
    response = simsimi(message)
    await msg.channel.send(response) # Will send Simsimi's reply to the chat where the message was forwarded

@client.event
async def on_ready():
  print(f"{client.user} is online!")

print(token)
client.run(token)