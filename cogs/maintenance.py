import discord
from bot import SosnowiecBot
from custom_cog import CustomCog
from discord import app_commands
from discord.ext import commands
from typing import List

class LogEmbed(discord.Embed):
    def __init__(self, action: str, description: str, success: bool, requestedBy: discord.User | discord.Member):
        super().__init__(
            title=action,
            description=description,
            color=discord.Color.green() if success else discord.Color.red()
        )

        self.add_field(name="Requested by", value=requestedBy.mention, inline=True)

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

    @app_commands.command(name="delete_messages")
    async def delete_messages(self, interaction: discord.Interaction, channel: discord.TextChannel, count: int):
        await interaction.response.defer(ephemeral=True, thinking=True)
        messages = [message async for message in channel.history(limit=count)]
        
        try:
            if len(messages) <= 100:
                await channel.delete_messages(messages)
            else:
                for message in messages:
                    await message.delete()
        
            embed = LogEmbed(
                action=f"🗑️ Usunięcie {len(messages)} wiadomości!",
                description=f"Usunięto {len(messages)} wiadomości na kanale {channel.mention}",
                requestedBy=interaction.user,
                success=True
            )
            await interaction.followup.send(f"Usunięto {len(messages)} wiadomości!")
            await self.log_channel.send(embed=embed)
        except Exception as e:
            print(e)
            embed = LogEmbed(
                action=f"🗑️ Usunięcie {len(messages)} wiadomości na kanale {channel.mention}!",
                description=f"Błąd: {e}",
                requestedBy=interaction.user,
                success=False
            )
            await self.log_channel.send(embed=embed)

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
                embed = LogEmbed(
                    action="🔄 Module Reloaded",
                    description=f"The extension {module} was successfully reloaded.",
                    success=True,
                    requestedBy=interaction.user
                )
                await self.log_channel.send(embed=embed)
        except Exception as e:
            await interaction.followup.send(f"Failed to reload '{module}'. Error: {e}", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(Maintenance(bot))