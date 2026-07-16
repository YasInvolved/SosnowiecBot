import discord
from custom_cog import CustomCog
from bot import SosnowiecBot
from discord.ext import commands

class Members(CustomCog):
    def __init__(self, bot: SosnowiecBot):
        super().__init__(bot)

    @commands.Cog.listener(name='on_member_join')
    async def on_member_join(self, member: discord.Member):
        await member.add_roles(self.unverified_role)
        
        embed = discord.Embed(
            title=f"👋 Witamy {member.mention}",
            description="Na początek zapoznaj się z tymi kanałami:",
            color=discord.Color.green()
        )
        embed.add_field(name="Regulamin", value=f"{self.rules_channel.mention}", inline=True)

        try:
            await self.welcome_channel.send(embed=embed)
        except Exception as e:
            print(f"Exception (on_member_join): {e}")

async def setup(bot: commands.Bot):
    await bot.add_cog(Members(bot))