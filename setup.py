from setuptools import find_packages, setup

setup(
    name='meme-machine-bot',
    version='0.1',
    description='Think of all the activities!',
    license='MIT',
    install_requires=[
        'discord.py==1.4.1',
        'requests==2.25.1'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'meme-machine-bot=meme_machine:main',
        ],
    }
)
