import discord
import os
import asyncio
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Signed in: {bot.user} (ID: {bot.user.id})')
    try:
        # Sync global commands
        synced = await bot.tree.sync()
        print(f'Synchronized {len(synced)} global commands.')
        
    except Exception as e:
        print(f'Synchronization error: {e}')

async def load_extensions():
    extensions = [
        'active', 
        'commands.general', 
        'commands.clear', 
        'commands.gemini', 
        'commands.nsfw',
        'commands.mod'
    ]
    for ext in extensions:
        try:
            await bot.load_extension(ext)
            print(f'Loaded: {ext}')
        except Exception as e:
            print(f'Error ({ext}): {e}')

async def main():
    async with bot:
        await load_extensions()
        token = os.getenv('DISCORD_TOKEN')
        if not token:
            print("ERROR: DISCORD_TOKEN not found in .env!")
            return
        await bot.start(token)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot shutting down...")