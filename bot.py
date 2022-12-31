import discord
import main_bot_logic
import json
from discord.ext import commands, tasks
from keep_alive import keep_alive


with open('config.json', 'r') as cfg:
  TOKEN = json.load(cfg)
bot = commands.Bot(command_prefix='$',
                    intents=discord.Intents.all(),
                    case_insensitive=True,
                    self_bot=True)


@bot.event
async def on_ready():
  print("bot works")
  geting_wot_news_from_rykoszet_webpage.start()


@tasks.loop(seconds=3600)
async def geting_wot_news_from_rykoszet_webpage():
  base_url = None
  while True:
    is_update, urls = main_bot_logic.main(base_url)
    if is_update:
      base_url = urls[0]
      for url in urls:
        channel = bot.get_channel(1053402661967368203)
        await channel.send(url)

keep_alive()
bot.run(TOKEN["token"])
