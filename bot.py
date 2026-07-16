import discord
import random
import os
from discord.ext import commands
from config import Config

class SosnowiecBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.guilds = True

        self.config = Config()

        super().__init__(
            command_prefix=f"{random.randbytes(128)}",
            intents=intents,
            help_command=commands.DefaultHelpCommand()
        )

    async def on_ready(self):
        print(f"Logged in as {self.user.name} (ID: {self.user.id})")

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

        guild_id = discord.Object(id=self.config.guild_id)

        try:
            self.tree.copy_global_to(guild=guild_id)
            synced = await self.tree.sync(guild=guild_id)
            print(f"Synced {len(synced)} command(s) to the server.")
        except Exception as e:
            print(f"Failed to sync commands: {e}")