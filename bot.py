
import discord
import os

TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
    channel = client.get_guild(662153006787199046)
    role = discord.utils.get(message.guild.roles, name='NotCertified')
    await member.add_roles(role)
client.run(TOKEN)
