from typing import Callable, List, Coroutine

import discord

CLIENT:               discord.Client = discord.Client()
ON_MESSAGE_QUEUE:     List[Callable[[discord.Message], Coroutine]] = []


@CLIENT.event
async def on_message(message: discord.Message):
    for callback in ON_MESSAGE_QUEUE:
        await callback(message)
