import discord
from discord.ext import commands

class Active(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.sent = False

    @commands.Cog.listener()
    async def on_ready(self):
        if self.sent: return
        for guild in self.bot.guilds:
            channel = guild.system_channel
            if not channel:
                channel = next((c for c in guild.text_channels if c.permissions_for(guild.me).send_messages), None)
            if channel:
                await channel.send("Power on")
        self.sent = True

async def setup(bot):
    await bot.add_cog(Active(bot))