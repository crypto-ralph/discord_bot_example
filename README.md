# discord_bot_example

This simple piece of codes shows how to create Discord bot in Python using library discord.py. 

Actions covered in the example:
- initializing client object
- connecting to a guild
- perform action after succesful connection
- replying to the DM
- creating cyclic events
- sending message top the specified channel
- getting user list
- getting channels list
- simple error handling

## Configuration
To ensure token safety [decouple](https://pypi.org/project/python-decouple/) library has been used. 
`.env` file is needed to provide token and guild name to the bot.  It should contain following config: 

```
TOKEN=<your_token_here>
GUILD=<your_guild name_here>
```

## Useful materials
Full tutorial about creating a discord bot including creating discord development account and generating token can 
be found here:  https://realpython.com/how-to-make-a-discord-bot-python/

Documentation of discord.py library:  https://discordpy.readthedocs.io/en/stable/

# License 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

For the details refer to LICENSE.md file