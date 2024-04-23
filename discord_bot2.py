import discord
import os
from discord.ext import commands

TOKEN = os.getenv('BOT_II_TOKEN')
client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print(f"{client.user} has connected to discord!")

@client.event
async def on_message(message):
    msg = message.content
    if message.author == client.user:
        return

    if msg.startswith("goodnight bot"):
        await message.channel.send(f"goodnight {message.author.mention}")

# for kicking members
@client.command()
# @commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None): 
    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} have been kicked sucessfully")

# for banning members
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason=None):
  await user.ban(reason=reason)
  await ctx.send(f"{user.mention} have been bannned sucessfully")


# for unbanning members
@client.command()
async def unban(ctx, *, member):
  banned_users = await ctx.guild.bans()
  member_name, member_discriminator = member.split('#')

  for ban_entry in banned_users:
    user = ban_entry.user
  
  if (user.name, user.discriminator) == (member_name, member_discriminator):
    await ctx.guild.unban(user)
    await ctx.send(f"{user.name} have been unbanned sucessfully")
    return


client.run(TOKEN)



