import discord
from bot import SosnowiecBot
from discord import app_commands
from discord.ext import commands

class Maintenance(commands.Cog):
    def __init__(self, bot: SosnowiecBot):
        self.bot = bot
        self.config = self.bot.config

    @property
    def guild(self) -> discord.Guild:
        return self.bot.get_guild(self.bot.config.guild_id)
    
    @property
    def technician_role(self) -> discord.Role:
        return self.guild.get_role()

    @property
    def log_channel(self) -> discord.TextChannel:
        return self.bot.get_channel(self.bot.config.log_channel_id)

    @app_commands.command(name="hello")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello")

    @app_commands.command(name="reload_module")
    async def reload_module(self, interaction: discord.Interaction, module: str):
        name = f"cogs.{module}"
        if name not in self.bot.extensions:
            await interaction.response.send_message(f"No module named '{module}'", ephemeral=True)
            return

        await interaction.response.defer(ephemeral=True)

        try:
            await self.bot.reload_extension(name)
            await interaction.followup.send(f"Reloaded {name}!", ephemeral=True)
            
            embed = discord.Embed(
                title="🔄 Module Reloaded",
                description=f"The extension {name} was successfully reloaded.",
                color=discord.Color.green()
            )
            embed.add_field(name="Requested By", value=interaction.user.mention, inline=True)
            for channel in self.bot.get_all_channels():
                print(channel.name)
            await self.log_channel.send(embed=embed)
        except Exception as e:
            await interaction.followup.send(f"Failed to reload '{name}'. Error: {e}", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(Maintenance(bot))