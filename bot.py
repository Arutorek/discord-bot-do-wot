import discord
import main_bot_logic
import json
from discord.ext import commands, tasks


with open('config.json', 'r') as cfg:
  TOKEN = json.load(cfg)
bot = commands.Bot(command_prefix='$',
                    intents=discord.Intents.all(),
                    case_insensitive=True,
                    self_bot=True)
bot.remove_command("help")


@bot.event
async def on_ready():
  print("bot works")
  geting_wot_news_from_rykoszet_webpage.start()


@tasks.loop(seconds=2)
async def geting_wot_news_from_rykoszet_webpage():
  channel = bot.get_channel(1058156429606920212)
  async for message in channel.history(limit=100):
    if message.author == bot.user:
      last_url = message.content
      break
  urls, is_update = main_bot_logic.main(last_url)
  if is_update:
    for url in urls:
      # channel = bot.get_channel(1053402661967368203)
      await channel.send(url)


@bot.command(name="help")
async def help(ctx):
    embed = discord.Embed(title="Help", description="Pomoc od BotDoWot")
    embed.add_field(name="Główne zadania bota:", value="Pobieranie  z internetu i wysyłanie na serwer informacji o nowościach w grze World of Tanks.")
    await ctx.channel.send(embed=embed)

bot.run(TOKEN["token"])
