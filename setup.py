from setuptools import find_packages, setup

setup(
    name='meme-machine-bot',
    version='0.1',
    description='Think of all the activities!',
    license='MIT',
    install_requires=[
        'discord.py'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'meme-machine-bot=meme_machine:run_lul_check',
        ],
    }
)
