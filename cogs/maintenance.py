import discord
from bot import SosnowiecBot
from custom_cog import CustomCog
from discord import app_commands
from discord.ext import commands
from typing import List

class Maintenance(CustomCog):
    def __init__(self, bot: SosnowiecBot):
        super().__init__(bot)

    async def module_autocomplete(self, interaction: discord.Interaction, current: str) -> List[app_commands.Choice[str]]:
        loaded_extensions = list(self.bot.extensions.keys())
        choices = [
            app_commands.Choice(name=ext, value=ext)
            for ext in loaded_extensions if current.lower() in ext.lower()
        ]

        return choices[:25]

    @app_commands.command(name="reload_module")
    @app_commands.autocomplete(module=module_autocomplete)
    async def reload_module(self, interaction: discord.Interaction, module: str, silent: bool = False):
        if module not in self.bot.extensions:
            await interaction.response.send_message(f"No module named '{module}'", ephemeral=True)
            return

        await interaction.response.defer(ephemeral=True)

        try:
            await self.bot.reload_extension(module)
            await interaction.followup.send(f"Reloaded {module}!", ephemeral=True)
            
            if not silent:
                embed = discord.Embed(
                    title="🔄 Module Reloaded",
                    description=f"The extension {module} was successfully reloaded.",
                    color=discord.Color.green()
                )
                embed.add_field(name="Requested By", value=interaction.user.mention, inline=False)
                await self.log_channel.send(embed=embed)
        except Exception as e:
            await interaction.followup.send(f"Failed to reload '{module}'. Error: {e}", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(Maintenance(bot))