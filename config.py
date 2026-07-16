from dataclasses import dataclass, field
from dotenv import dotenv_values

CONFIG = dotenv_values(".env")

@dataclass
class Config:
    _env = dotenv_values(".env")

    token: str = field(
        default_factory=lambda: CONFIG.get("TOKEN")
    )

    guild_id: int = field(
        default_factory=lambda: int(CONFIG.get("GUILD_ID"))
    )

    log_channel_id: int = field(
        default_factory=lambda: int(CONFIG.get("LOG_CHANNEL_ID"))
    )