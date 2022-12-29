import discord
import main_bot_logic
import json
from discord.ext import commands
from keep_alive import keep_alive


def run_discord_bot():
  with open('config.json', 'r') as cfg:
    TOKEN = json.load(cfg)
  bot = commands.Bot(command_prefix='$',
                     intents=discord.Intents.all(),
                     case_insensitive=True,
                     self_bot=True)

  @bot.command(name="start")
  async def geting_wot_news_from_rykoszet_webpage(ctx):
    base_url = None
    while True:
      is_update, url = main_bot_logic.main(base_url)
      if is_update:
        base_url = url
        channel = bot.get_channel(1053402661967368203)
        await channel.send(url)
      else:
        channel = bot.get_channel(1054842860144431134)
        await channel.send("No update form 'rykoszet.info' yet")

  keep_alive()
  bot.run(TOKEN["token"])
