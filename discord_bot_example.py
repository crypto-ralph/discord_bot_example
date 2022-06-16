"""
This code provide functional implementation of Discord bot. To be able to run it .env file with the
following code is needed:
TOKEN=<your_token_here>
GUILD=<your_guild name_here>

For more information please refer to the README file.
"""

from discord import Intents
from discord import utils
from discord.ext import commands
from discord.ext import tasks

from decouple import config

# Values extracted from .env file
TOKEN = config('TOKEN')
GUILD = config('GUILD')


# Intents.members must be enabled to use fetch_members
intents = Intents.default()
intents.members = True  # pylint: disable=E0237

client = commands.Bot(command_prefix=',', intents=intents)


@client.event
async def on_ready():
    """
    Event that executes always after succesfull startup.
    In this example on startup list of server members and channels is printed to console log.
    :return:
    """
    guild = utils.get(client.guilds, name=GUILD)
    print(f'{client.user} has connected to following guild: {guild.name}(id: {guild.id})')

    print('*** Members ***')
    async for member in guild.fetch_members(limit=150):
        print(f'Member name: {member.name} id: {member.id}')

    print('*** Channels ***')
    for channel in guild.text_channels:
        print(f'Channel name: {channel.name} id: {channel.id}')


@client.event
async def on_member_join(member):
    """
    Executes when new user joins guild.

    :param member: Member object which allows comunication with member during handling this event.
    :return:
    """
    print(f'Member name: {member.name}')
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the this Discord server. Enjoy!'
    )


@client.event
async def on_message(message):
    """
    Handles messages sent directly to the bot.

    :param message: object representing message that has been sent by user
    :return:
    """
    if message.author == client.user:
        # It prevents handling here messages sent by bot to user
        return

    print(f'Msg guild: {message.guild}')
    print(f'Msg author: {message.author}')
    print(f'Msg content: {message.content}')

    await message.author.send('Thank you for your message')


@client.event
async def on_error(event: str, *args):
    """
    Error handling routine. In this example error message is logged to console log and also to the
    err.log file created in root directory.
    :param event: string containing name of routine that raised an error.
    :param args: Tuple with error information.
    :return:
    """
    with open('err.log', 'a', encoding='UTF-8') as error_file:
        if event == 'on_message':
            print(f'ERROR: Unhandled message: {args[0]}')
            error_file.write(f'Unhandled message: {args[0]}\n')
        else:
            print(f'ERROR: Other error in event {event}: {args[0]}')
            error_file.write(f'Other error: {args}\n')


@tasks.loop(seconds=50)
async def my_task():
    """
    This is example of periodic tast executed every certain time period after succesful start.
    This task will send test message every 50 seconds to first channel on guild channel list.
    :return:
    """
    guild = utils.get(client.guilds, name=GUILD)
    await guild.text_channels[0].send('test msg')


@my_task.before_loop
async def before_my_task():
    """
    This routine is a custom routine which will be executed before creating bot client and
    connecting to the Discord guild. Some operations which are needed before connection can be
    placed here i.e. backend iniialization.
    :return:
    """
    await client.wait_until_ready()

my_task.start()
client.run(TOKEN)
