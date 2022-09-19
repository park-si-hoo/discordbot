import discord

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('다음으로 로그인합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=None)

bot.run('MTAyMTM1MjI4NjU2NTQzMzM2NA.G1OL87.g-AmMOHKDfPtXNyeZkPez_naz4MDYxk9U0Qifs')
