import re
from json import dumps
from typing import Match, Callable, Dict

import discord

from meme_machine.client import CLIENT

_REACTION_COMMAND_MATCH = r'!reaction (add|remove|display|help) ?(\w+|\".+?\")? ?(\w+|\".+\")?'
_REACTION_COMMAND_HELP = ('Available commands:\n'
                          '!reaction add "trigger text" "response text"\n'
                          '    - Adds the trigger text to the reaction data-store.\n'
                          '!reaction remove "trigger text"\n'
                          '    - Removes the trigger and reaction from the data-store.\n'
                          '!reaction display\n'
                          '    - Displays the current reaction data-store.\n'
                          '!reaction help\n'
                          '    - Displays this help message.')


def normalize(text: str) -> str:
    return ''.join(char for char in text.lower() if 97 <= ord(char) <= 122 or ord(char) == 32)


async def _parse_reaction(message: discord.Message, match: Match[str]):
    command = match.group(1)
    if command in _REACTION_COMMAND_MAP:
        await _REACTION_COMMAND_MAP[command](message, match)


async def _handle_add(_: discord.Message, match: Match[str]):
    groups = [group.replace('"', '') for group in match.groups()]
    if len(groups) < 3:
        return

    _REACTION_STORE[normalize(groups[1])] = groups[2]


async def _handle_remove(_: discord.Message, match: Match[str]):
    groups = [group.replace('"', '') if group else group for group in match.groups()]
    if len(groups) < 2:
        return

    if groups[1] in _REACTION_STORE:
        del _REACTION_STORE[normalize(groups[1])]


async def _handle_display(message: discord.Message, _: Match[str]):
    await message.channel.send(message, dumps(_REACTION_STORE, sort_keys=True, indent=4))


async def _handle_help(message: discord.Message, _: Match[str]):
    await message.channel.send(_REACTION_COMMAND_HELP)


async def on_message(message: discord.Message):
    if message.author == CLIENT.user:
        return

    content: str = message.content
    match = re.search(_REACTION_COMMAND_MATCH, content)

    if match:
        await _parse_reaction(message, match)
    else:
        reaction = _REACTION_STORE.get(normalize(content))

        if reaction:
            await message.channel.send(reaction)


_REACTION_STORE:       Dict[str, str] = {}
_REACTION_COMMAND_MAP: Dict[str, Callable[[discord.Message, Match[str]], None]] = {
    'add': _handle_add,
    'remove': _handle_remove,
    'display': _handle_display,
    'help': _handle_help,
}
