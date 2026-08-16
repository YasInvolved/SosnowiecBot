import discord
import io
from utils.wg_easy import WgEasyAdapter
from custom_cog import CustomCog
from bot import SosnowiecBot
from discord import app_commands
from discord.ext import commands

class Minecraft(CustomCog):
    def __init__(self, bot: SosnowiecBot):
        super().__init__(bot)

    @app_commands.command(name="teren", description="Zarejestruj swój teren")
    async def register_plot(self, interaction: discord.Interaction, nazwa: str, x: int, z: int, rozmiar_x: int, rozmiar_z: int):
        embed = discord.Embed(
            title="ℹ️ Nowy teren!",
            color=discord.Color.green()
        )

        try:
            embed.add_field(name="Nazwa", value=nazwa, inline=False)
            embed.add_field(name="X", value=str(x), inline=True)
            embed.add_field(name="Z", value=str(z), inline=True)
            embed.add_field(name="Rozmiar X", value=str(rozmiar_x), inline=True)
            embed.add_field(name="Rozmiar Z", value=str(rozmiar_z), inline=True)
            embed.add_field(name="Właściciel", value=f"{interaction.user.mention}", inline=False)

            await self.plots_channel.send(embed=embed)
            await interaction.response.send_message("Działka zarejestrowana!", ephemeral=True)
        except Exception as e:
            print(e)
            await interaction.response.send_message("Wystąpił błąd", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(Minecraft(bot))