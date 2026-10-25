import os
import discord
from discord.ext import commands
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
 @bot.event
async def on_ready():
  print(f"bot is online:{bot.user}")

  @bot.command()
  async def motivate (ctx);
  await ctx.send("welcome! Study for 25 minutes, then take a short break.")
  @bot.command()
  async def motivate(ctx):
    await ctx.send("keep learning! Every small step counts.")

@bot.command()
asynx def helpme(ctx):
  await ctx.send("Commands: !study, ! motivate, !helpme")

bot.run(os.environ["DISCORD_TOKEN"])
