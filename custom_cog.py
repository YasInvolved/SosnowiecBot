import discord
import os
from discord.ext import commands
from bot import SosnowiecBot

class CustomCog(commands.Cog):
    def __init__(self, bot: SosnowiecBot):
        self.bot = bot
        self.config = self.bot.config
        self.content_dir = os.path.join(os.path.curdir, "content")
    
    def get_content_filename(self, relpath: str) -> str:
        return os.path.join(self.content_dir, relpath)

    @property
    def guild(self) -> discord.Guild:
        return self.bot.get_guild(self.config.guild_id)
    
    # channels
    @property
    def log_channel(self) -> discord.TextChannel:
        return self.bot.get_channel(self.config.log_channel_id)
    
    @property
    def rules_channel(self):
        return self.guild.get_channel(self.config.rules_channel_id)
    
    @property
    def welcome_channel(self):
        return self.guild.get_channel(self.config.welcome_channel_id)
    
    @property
    def plots_channel(self) -> discord.TextChannel:
        return self.guild.get_channel(self.config.plots_channel_id)

    # roles
    @property
    def unverified_role(self):
        return self.guild.get_role(self.config.unverified_role_id)
    
    @property
    def verified_role(self):
        return self.guild.get_role(self.config.verified_role_id)