import discord
from discord.ext import commands
import responses

# from discord.ext import commands

# client = commands.Bot(command_prefix= "?")

# client.run("MTA1MzQ0MzE1MjcwNDQ0MjQxOQ.GJYzzv.ctVpWNszTh_9z-9447dB3AOXOQdJ2V2U-j9G2g")

async def send_message(message, user_message, is_private):
    try:
        response = responses.hanle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = 'MTA1NTA5MzQ3Nzc5MDE4NzU4MQ.GbkKTC.wmSfBMKd3gnkuuLsUk7PtIqI30IDmqybcoz_jM '
    # intents = discord.Intents.default()
    # intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=discord.Intents.all(), case_insensitive=True, self_bot=True)
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message == '':
            await send_message(message, user_message, is_private=False)
        elif user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)


    @bot.command(pass_context=True)
    async def ping(ctx):
        channel = bot.get_channel(1053402661967368203)
        await channel.send('test')

    client.run(TOKEN)
