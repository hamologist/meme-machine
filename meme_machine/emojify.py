import re
from os import getenv

import discord
import requests

_EMOJIFY_URL: str = getenv('MEME_MACHINE_EMOJIFY_URL')
_EMOJIFY_COMMAND_MATCH = r'!emojify (.+)'


async def on_message(message: discord.Message):
    content: str = message.content
    match = re.search(_EMOJIFY_COMMAND_MATCH, content)

    if match:
        response = requests.post(_EMOJIFY_URL, json={
            'message': match.group(1)
        })

        try:
            data = response.json()
            emojification = data.get('Message')
            if emojification:
                await message.channel.send(emojification)
        except:
            pass

if not _EMOJIFY_URL:
    raise Exception("Missing MEME_MACHINE_EMOJIFY_URL environment variable.")
