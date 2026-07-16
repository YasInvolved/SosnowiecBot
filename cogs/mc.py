import discord
from custom_cog import CustomCog
from bot import SosnowiecBot
from discord import app_commands
from discord.ext import commands

class Minecraft(CustomCog):
    def __init__(self, bot: SosnowiecBot):
        super().__init__(bot)

    @app_commands.command(name="teren", description="Zarejestruj swój teren")
    async def register_plot(self, interaction: discord.Interaction, nazwa: str, x: int, y: int):
        embed = discord.Embed(
            title="ℹ️ Nowy teren!",
            color=discord.Color.green()
        )

        embed.add_field(name="Nazwa", value=nazwa, inline=False)
        embed.add_field(name="Koordynaty", value=f"{x}, {y}", inline=False)
        embed.add_field(name="Właściciel", value=f"{interaction.user.mention}", inline=False)
        embed.set_image(url="attachment://jasper-wow.gif")

        try:
            gif = discord.File(self.get_content_filename("jasper-iphone-wow.gif"), filename="jasper-wow.gif")
            await self.plots_channel.send(file=gif, embed=embed)
            await interaction.response.send_message("Działka zarejestrowana!", ephemeral=True)
        except Exception as e:
            print(e)
            await interaction.response.send_message("Wystąpił błąd", ephemeral=True)

async def setup(bot: commands.Bot):
    await bot.add_cog(Minecraft(bot))