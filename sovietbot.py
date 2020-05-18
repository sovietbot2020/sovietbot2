import discord
import asyncio
from discord.ext import commands
import random
from discord.utils import get


client = commands.Bot(command_prefix='크리스')

token = "NzExNjM0ODM5NjA1ODcwNjkz.XsJk8w.DZpGFjsWUUNkaH5wiAcSH4UJc78"

@client.event
async def on_ready():

    print("=========================")
    print("다음으로 로그인 합니다 : 소련여자")
    print(client.user.name)
    print("connection was successful")
    game = discord.Game("나다, Hamsters.")
    print("=========================")
    await client.change_presence(status=discord.Status.online, activity=game)
                                     

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "안녕 크리스":
        await message.channel.send("안녕 Hamster")
               

@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author.bot:
        return None
    if message.content == "크리스 계산":
        await message.channel.send("나다, Hamster.")
    if message.content.startswith("크리스1부터10"):
        for x in range(10):
            await message.channel.send(x+1)
    if message.content.startswith("크리스"):
        global calcResult
        param = message.content.split()
        try:
            if param[1].startswith("더하기"):
                calcResult = int(param[2])+int(param[3])
                await message.channel.send("쉽네, "+str(calcResult))
            if param[1].startswith("빼기"):
                calcResult = int(param[2])-int(param[3])
                await message.channel.send("쉽네, "+str(calcResult))
            if param[1].startswith("곱하기"):
                calcResult = int(param[2])*int(param[3])
                await message.channel.send("쉽네, "+str(calcResult))
            if param[1].startswith("나누기"):
                calcResult = int(param[2])/int(param[3])
                await message.channel.send("쉽네. "+str(calcResult))
        except IndexError:
            await message.channel.send("무슨 숫자를 계산할지 말을 해라")
        except ValueError:
            await message.channel.send("숫자로 입력해라")
        except ZeroDivisionError:
            await message.channel.send("You can't divide with 0.")

@client.command(pass_context=True)
async def 랜덤숫자(ctx, num1, num2):
    picked = random.randint(int(num1), int(num2))
    await ctx.send(''+str(picked))

@commands.has_permissions(administrator=True)

@client.command(name="추방", pass_context=True)
async def _kick(ctx, *, user_name: discord.Member, reason=None):
    await user_name.kick(reason=reason)
    await ctx.send(str(user_name)+", 이 사람은 Hamsters 아니다.")

@_kick.error
async def _kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("나다, Hamster. 너는 이 명령어를 실행할 권한이 없다.".format(ctx.message.author))
    
@client.command(name="뮤트", pass_context=True)
async def _mute(ctx, member: discord.Member=None):
    member = member or ctx.message.author
    await member.add_roles(get(ctx.guild.roles, name="Muted"))
    await ctx.send(str(member)+" 쉿! 아무 말 하지 마 내 Baby Hamster.")

@client.command(name="언뮤트", pass_context=True)
async def _unmute(ctx, member: discord.Member=None):
    member = member or ctx.message.author
    await member.remove_roles(get(ctx.guild.roles, name='Muted'))
    await ctx.send(str(member)+" Go, Hamster.")




client.run(token)
