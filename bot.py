
import discord
import os

TOKEN = os.environ.get("DISCORD_TOKEN")

client = discord.Client()

guild = client.get_guild(662153006787199046)

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
    await channel.send(embed=embed)
    role = discord.utils.find(lambda r: r.name == 'NotCertified', member.guild.roles)  
    await member.add_roles(role) 
async def on_member_remove(member):
    channel = client.get_channel(673782210771550229)
    embed = discord.Embed(title="Joined",description = f'{str(member)}が退出。',color=discord.Colour.from_rgb(255, 0, 0))
    await channel.send(embed=embed)
client.run(TOKEN)
