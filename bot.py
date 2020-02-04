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
    await channel.send('インターネットのルールをしっかり守れないと処罰されますよ！\nここはBOTの開発のテストサーバーも兼ねてるので通知がうるさいかも！\nそれでもいいよってひとは下の:white_check_mark: をおしてね！')

@client.event
async def on_member_join(member):
    #入退室ログ
    channel = client.get_channel(673782210771550229)
    embed = discord.Embed(title="Joined",description = f'@{str(member)}が参加。',color=discord.Colour.from_rgb(0, 255, 255))
    await channel.send(embed=embed)
    role = discord.utils.find(lambda r: r.name == 'NotCertified', member.guild.roles)  
    await member.add_roles(role)
    
@client.event
async def on_member_remove(member):
    channel = client.get_channel(673782210771550229)
    embed = discord.Embed(title="Joined",description = f'@{str(member)}が退出。',color=discord.Colour.from_rgb(255, 0, 0))
    await channel.send(embed=embed)
    channel = client.get_channel(674169297001775114)
    embed = discord.Embed(title="Joined",description = f'@{str(member)}さんが退出...さようなら...また逢う日まで',color=discord.Colour.from_rgb(255, 0, 0))
    await channel.send(embed=embed)
    
#リアクションで参加   
ID_CHANNEL_README = 673798279552565268
ID_ROLE_WELCOME = 663566271446515758
@client.event  
async def on_raw_reaction_add(payload):  
    channel = client.get_channel(payload.channel_id)  
    if channel.id == ID_CHANNEL_README:  
        guild = client.get_guild(payload.guild_id)  
        member = guild.get_member(payload.user_id)
        role = guild.get_role(ID_ROLE_WELCOME)  
        await member.add_roles(role)
        channel = client.get_channel(674169297001775114)
        role = discord.utils.find(lambda r: r.name == 'NotCertified', member.guild.roles)  
        await member.remove_roles(role)
        role = discord.utils.find(lambda r: r.name == '082', member.guild.roles)  
        await member.add_roles(role)
        embed = discord.Embed(title="Joined",description = f'@{str(member)}がジャガの部屋に来たよ！よろしく！ :smile:',color=discord.Colour.from_rgb(0, 255, 255))
        await channel.send(embed=embed)
        await remove_reaction(✅, member)
client.run(TOKEN)
