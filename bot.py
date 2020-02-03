
import discord
import os

TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    channel = client.get_channel(673798279552565268)
    await channel.purge()
    await channel.send('**ジャガの部屋へようこそ！**\nわいわい雑談・ゲームしたりしましょう！:smile:\n招待リンクです→→ https://discord.gg/uGUKFPb')

@client.event
async def on_member_join(member):
    #入退室ログ
    channel = client.get_channel(673782210771550229)
    embed = discord.Embed(title="Joined",description = f'{str(member)}が参加。',color=discord.Colour.from_rgb(0, 255, 255))
    await message.channel.send(embed=embed)
    role = discord.utils.get(message.guild.roles, name='NotCertified')
    await member.add_roles(role)
    channel = 
async def on_member_remove(member):
    channel = client.get_channel(673782210771550229)
    embed = discord.Embed(title="Joined",description = f'{str(member)}が退出。',color=discord.Colour.from_rgb(255, 0, 0))
    await message.channel.send(embed=embed)
client.run(TOKEN)