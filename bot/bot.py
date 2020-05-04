import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
client = discord.Client()
id = client.get_guild(660943145105883156)

@client.event
async def on_member_update(before, after):
   print(after.activity)
   guild = after.guild
   if after.activity != None:
      if after.activity.name == "League of Legends":
         b = discord.utils.get(guild.voice_channels, name='league-of-legends', bitrate=64000)
         await after.move_to(b)
      if after.activity.name == "ROBLOX":
         b = discord.utils.get(guild.voice_channels, name='roblox', bitrate=64000)
         await after.move_to(b)
client.run("NzA1ODg0MDIwNzc2MzcwMjQ5.Xq6dmw.cImO50OpzQPTRu7Sq7CGfDAJlOg")     
