import discord
from discord import app_commands
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="kick", description="Kicks the specified user from the server.")
    @app_commands.describe(member="Member to kick", reason="Reason")
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
        if member.id == interaction.user.id:
            await interaction.response.send_message("You cannot kick yourself!", ephemeral=True)
            return
        
        try:
            await member.kick(reason=reason)
            await interaction.response.send_message(f"{member.mention} has been kicked from the server. Reason: {reason}")
        except discord.Forbidden:
            await interaction.response.send_message("Insufficient permissions to kick this user (check role hierarchy).", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"An error occurred: {e}", ephemeral=True)

    @app_commands.command(name="ban", description="Bans the specified user from the server.")
    @app_commands.describe(member="Member to ban", reason="Reason")
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str = "No reason provided"):
        if member.id == interaction.user.id:
            await interaction.response.send_message("You cannot ban yourself!", ephemeral=True)
            return

        try:
            await member.ban(reason=reason)
            await interaction.response.send_message(f"{member.mention} has been banned from the server. Reason: {reason}")
        except discord.Forbidden:
            await interaction.response.send_message("Insufficient permissions to ban this user (check role hierarchy).", ephemeral=True)
        except Exception as e:
            await interaction.response.send_message(f"An error occurred: {e}", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Moderation(bot))