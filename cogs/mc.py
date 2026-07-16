import discord
from custom_cog import CustomCog
from bot import SosnowiecBot
from discord import app_commands
from discord.ext import commands

class Minecraft(CustomCog):
    def __init__(self, bot: SosnowiecBot):
        super().__init__(bot)

    @app_commands.command(name="teren", description="Zarejestruj swój teren")
    async def register_plot(self, interaction: discord.Interaction, nazwa: str, x: int, y: int, rozmiar_x: int, rozmiar_y: int):
        embed = discord.Embed(
            title="ℹ️ Nowy teren!",
            color=discord.Color.green()
        )

        try:
            embed.add_field(name="Nazwa", value=nazwa, inline=False)
            embed.add_field(name="X", value=str(x), inline=True)
            embed.add_field(name="Y", value=str(y), inline=True)
            embed.add_field(name="Rozmiar X", value=str(rozmiar_x), inline=True)
            embed.add_field(name="Rozmiar Y", value=str(rozmiar_y), inline=True)
            embed.add_field(name="Właściciel", value=f"{interaction.user.mention}", inline=False)
            embed.set_image(url="attachment://jasper-wow.gif")

            gif = discord.File(self.get_content_filename("jasper-iphone-wow.gif"), filename="jasper-wow.gif")
            await self.plots_channel.send(file=gif, embed=embed)
            await interaction.response.send_message("Działka zarejestrowana!", ephemeral=True)
        except Exception as e:
            print(e)
            await interaction.response.send_message("Wystąpił błąd", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(Minecraft(bot))