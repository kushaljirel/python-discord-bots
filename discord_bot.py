import discord
import os 
import requests
import json
import random
from discord.ext import commands
TOKEN = os.getenv('BOT_I_TOKEN')

def get_quote():
    response = requests.get('https://zenquotes.io/api/random')
    # print(response)
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)

words = ["sad", "depressed", "depression", "unhappy"]

client = commands.Bot(command_prefix = '!')
# client = discord.Client()
encouraging_msg = ["Every thing will be fine", "Time Heals everyone just give yourself time", "Don't worry everything happens for good reason", "hang in there! everything is fine"]
@client.event
async def on_ready():
    print(f"{client.user} has connected to discord!")

@client.event
async def on_message(message):

    msg = message.content
    quote = get_quote()
    if message.author == client.user:
        return 
    
    if  msg.startswith("#hello"):
        await message.channel.send(f"{message.author.mention} hello there")

    greeting = ["hi mr.bot", "Hi! Mr.Bot", "Hi Mr.Bot", "hello mr.bot", "Hello! Mr.Bot", "Hello Mr.Bot"]

    if any(greet in msg for greet in greeting) :
        response = f"{message.author.mention} hello there."
        await message.channel.send(response)

    if any(word in msg for word in words):
        respond = f"{message.author.mention} {random.choice(encouraging_msg)}"
        await message.channel.send(respond) 
    
    if msg.startswith("#inspire"):
        await message.channel.send(quote)  

#kick command using discord.py

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason=None):
  await user.kick(reason=reason)
  await ctx.send(f"{user} have been kicked sucessfully")

# <----- kick commmand end ------>


# @bot.command()
# @commands.has_permissions(ban_members=True)
# async def ban(ctx, user: discord.Member, *, reason=None):
#   await user.ban(reason=reason)
#   await ctx.send(f"{user} have been bannned sucessfully")

# # for unbanning members
# @bot.command()
# async def unban(ctx, *, member):
#   banned_users = await ctx.guild.bans()
#   member_name, member_discriminator = member.split('#')

#   for ban_entry in banned_users:
#     user = ban_entry.user
  
#   if (user.name, user.discriminator) == (member_name, member_discriminator):
#     await ctx.guild.unban(user)
#     await ctx.send(f"{user} have been unbanned sucessfully")
#     return


client.run(TOKEN)
