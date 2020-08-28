import discord

from meme_machine.client import CLIENT


async def on_message(message: discord.Message):
    content: str = ''.join(char for char
                           in message.content.lower()
                           if 97 <= ord(char) <= 122 or ord(char) == 32)
    for token in content.split(' '):
        if token == 'lul':
            await message.channel.send('lol*')
