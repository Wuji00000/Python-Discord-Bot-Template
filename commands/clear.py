import discord
from discord.ext import commands
from discord import app_commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="delete_message", description="Deletes the specified number of messages.")
    @app_commands.describe(amount="Number of messages to delete")
    async def delete_message(self, interaction: discord.Interaction, amount: int):
        await interaction.response.send_message(f"Deleting {amount} messages...", ephemeral=True)
        if interaction.channel:
            await interaction.channel.purge(limit=amount)

async def setup(bot):
    await bot.add_cog(Clear(bot))