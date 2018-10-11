import logging
from asyncio import coroutine
from os import getenv

import discord

_MEME_MACHINE_TOKEN: str = getenv('MEME_MACHINE_TOKEN')
_LOGGER:             logging.Logger = logging.getLogger(__name__)
_CLIENT:             discord.Client = discord.Client()


@_CLIENT.event
@coroutine
def on_message(message: discord.Message):
    content: str = ''.join(char for char in message.content.lower() if 97 <= ord(char) <= 122)
    for token in content.split(' '):
        if token == 'lul':
            yield from _CLIENT.send_message(message.channel, 'lol*')


def main():
    if not _MEME_MACHINE_TOKEN:
        _LOGGER.fatal('Failed to provide a valid Discord API token')
        exit(1)

    _CLIENT.run(_MEME_MACHINE_TOKEN)
    _CLIENT.close()


if __name__ == '__main__':
    main()
