import discord
import random
import os
from utils.wg_easy import WgEasyAdapter
from discord.ext import commands
from config import Config

class SosnowiecBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.guilds = True

        self.config = Config()
        self.wg_easy = WgEasyAdapter()

        super().__init__(
            command_prefix=f"{random.randbytes(128)}",
            intents=intents,
            help_command=commands.DefaultHelpCommand()
        )

    @property
    def guild(self) -> discord.Guild:
        return self.get_guild(self.config.guild_id)
    
    async def on_ready(self):
        print(f"Logged in as {self.user.name} (ID: {self.user.id})")

    async def sync_tree(self):
        guild_id = discord.Object(id=self.config.guild_id)
        self.tree.copy_global_to(guild=guild_id)
        synced = await self.tree.sync(guild=guild_id)
        print(f"Synced {len(synced)} command(s) to the server.")

    async def setup_hook(self):
        for path in os.listdir("./cogs"):
            filename, ext = os.path.splitext(os.path.basename(path))
            if ext == ".py":
                module_name = f"cogs.{filename}"

            try:
                await self.load_extension(module_name)
                print(f"Loaded module: {module_name}")
            except Exception as e:
                print(f"Failed to load {module_name}: {e}")

        try:
            await self.sync_tree()
        except Exception as e:
            print(f"Failed to sync commands: {e}")