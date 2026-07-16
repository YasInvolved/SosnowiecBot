import discord
from bot import SosnowiecBot
from discord.ext import commands

class Members(commands.Cog):
    def __init__(self, bot: SosnowiecBot):
        self.bot = bot
        self.config = self.bot.config
        self.guild = self.bot.guild
    
    @property
    def unverified_role(self):
        return self.guild.get_role(self.config.unverified_role_id)

    @property
    def verified_role(self):
        return self.guild.get_role(self.config.verified_role_id)

    @property
    def welcome_channel(self):
        return self.guild.get_channel(self.config.welcome_channel_id)

    @property
    def rules_channel(self):
        return self.guild.get_channel(self.config.rules_channel_id)

    @commands.Cog.listener(name='on_member_join')
    async def on_member_join(self, member: discord.Member):
        await member.add_roles(self.unverified_role)
        
        embed = discord.Embed(
            title=f"👋 Witamy {member.mention}",
            description="Na początek zapoznaj się z tymi kanałami:",
            color=discord.Color.green()
        )
        embed.add_field(name="Regulamin", value=f"{self.rules_channel.mention}", inline=True)
        await self.welcome_channel.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Members(bot))