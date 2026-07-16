import asyncio
from bot import SosnowiecBot

async def main():
    bot = SosnowiecBot()

    async with bot:
        await bot.start(bot.config.token)

if __name__ == "__main__":
    asyncio.run(main())