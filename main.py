import os
import discord
from discord.ext import commands

from myserver import server_on

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())



# Bot event เมื่อบอทพร้อมใช้งาน
@bot.event
async def on_ready():
    print("bot online!")


  # แจ้งคนเข้า - ออกเซอร์เวอร์
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1429987075825995847) # ห้องที่บอทจะส่งข้องความ
    text = f"### สวัสดี {member.mention} สมาชิกไหม่ <a:yayblobhyper:1429900761965527140> ###" # ข้อความต้อนรับ
    if channel is None:
        channel = await bot.fetch_channel(1429987075825995847)
        await channel.send(text) # ส่งข้อความไปที่ห้อง


    embed = discord.Embed()
    await channel.send(text) # ส่งข้อความไปที่ห้องนี้


server_on()

bot.run(os.getenv('TOKEN'))