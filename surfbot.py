#
# Surfbot for discord
# Written by Ethan and Antonio for SBHacks 2021
# Written in Python 3.8
# Version 1.0
# This app leverages the MagicSeaweed API to pull local surf forecasts for local beaches
#

# importing the discord library to use functions
import discord
import json
import sys
sys.path.append('../')
from surfjson import *


# creating a Client object with the name client, from the discord library
client = discord.Client()

with open('./surfjson/trestles.json') as tj:
    data = json.load(tj)

# This is the main function that will send messages in discord
@client.event
# It is an async function, because it is running and looking for the word "!hello"
async def on_message(message):
    id = client.get_guild(796970280747794482)
    channels = ["bot-commands"]

    if str(message.channel) in channels:
        if message.content.find("!surf") != -1:
            # Once it receives !hello, it will respond hi
            await message.channel.send(json.dumps(data[0]['swell'], indent=2))
            await message.channel.send(json.dumps(data[0]['condition'], indent=2))

# This is the final function that will run the bot
# Token is removed for security
client.run("Token")