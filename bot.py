import discord
import main_bot_logic
from discord.ext import commands


def run_discord_bot():
    TOKEN = 'MTA1NTA5MzQ3Nzc5MDE4NzU4MQ.GxU-Pi.YIw__dI8CfJI_cGEU3_mmV5GF-gyOXxabagq24'
    bot = commands.Bot(command_prefix='$', intents=discord.Intents.all(), case_insensitive=True, self_bot=True)

    @bot.command(name="start")
    async def geting_wot_news_from_rykoszet_webpage(ctx):
        base_url = None
        while True:
            url = main_bot_logic.main(base_url)
            base_url = url
            channel = bot.get_channel(1053402661967368203)
            await channel.send(url)


    bot.run(TOKEN)
