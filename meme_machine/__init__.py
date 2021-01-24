import logging
from os import getenv

from meme_machine.client import CLIENT, ON_MESSAGE_QUEUE
from meme_machine import emojify, lul_check, reaction_processor

__MEME_MACHINE_TOKEN: str = getenv('MEME_MACHINE_TOKEN')
LOGGER:               logging.Logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.CRITICAL)


def main():
    if not __MEME_MACHINE_TOKEN:
        LOGGER.fatal('Failed to provide a valid Discord API token')
        exit(1)

    ON_MESSAGE_QUEUE.append(lul_check.on_message)
    ON_MESSAGE_QUEUE.append(reaction_processor.on_message)
    ON_MESSAGE_QUEUE.append(emojify.on_message)
    CLIENT.run(__MEME_MACHINE_TOKEN)
    CLIENT.close()


if __name__ == '__main__':
    main()
