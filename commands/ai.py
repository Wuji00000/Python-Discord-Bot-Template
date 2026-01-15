import discord
from discord.ext import commands
from discord import app_commands
import google.generativeai as genai
import os

class Gemini(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        api_key = os.getenv("ai_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
        else:
            print("ERROR: ai_API_KEY not found!")
    @app_commands.command(name="talk", description="Chat with Protocol.")
    @app_commands.describe(prompt="Your message...")
    async def talk(self, interaction: discord.Interaction, prompt: str):
        await interaction.response.defer()
        try:
            model = genai.GenerativeModel('gemini-2.5-flash', system_instruction="Your name is Protocol. You are a helpful, friendly Discord bot that gives short answers. Do not provide dictionary-style definitions; speak like a natural friend.")
            response = model.generate_content(prompt)
            response_text = response.text.strip()
            
            if len(response_text) <= 2000: await interaction.followup.send(response_text)
            else:
                for i in range(0, len(response_text), 2000): await interaction.followup.send(response_text[i:i+2000])
        except Exception as e: await interaction.followup.send(f"Error: {e}")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user: return
        if message.reference and message.reference.resolved:
            replied_message = message.reference.resolved
            if isinstance(replied_message, discord.Message) and replied_message.author == self.bot.user:
                async with message.channel.typing():
                    try:
                        model = genai.GenerativeModel('gemini-2.5-flash', system_instruction="Your name is Protocol. You are a helpful, friendly Discord bot that gives short answers. Do not provide dictionary-style definitions; speak like a natural friend.")
                        response = model.generate_content(message.content)
                        await message.reply(response.text.strip())
                    except Exception as e: await message.reply(f"Error: {e}")

async def setup(bot):
    await bot.add_cog(Gemini(bot))