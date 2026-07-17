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

    @app_commands.command(name="generuj_vpn", description="Generuje klienta do VPN")
    @app_commands.checks.has_role(1527114285711360141)
    async def generate_vpn(self, interaction: discord.Interaction):
        try:
            if interaction.user.get_role(self.config.vpn_role_id):
                await interaction.response.send_message("Masz już klienta.", ephemeral=True)

            await interaction.response.defer(thinking=True, ephemeral=True)
            async with WgEasyAdapter() as wg:
                config_id = await wg.create_client(f"{interaction.user.name}_{interaction.user.id}")
                cfg_data = await wg.get_client_config_stream(config_id)
            
            cfg_file = discord.File(cfg_data, filename=f"{interaction.user.name}.cfg")
            await interaction.user.add_roles(discord.Object(id=self.config.vpn_role_id))
            await interaction.followup.send("Wygenerowano klienta!", file=cfg_file)
        except Exception as e:
            print(f"Error: {e}")

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