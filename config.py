from dataclasses import dataclass, field
from dotenv import dotenv_values

CONFIG = dotenv_values(".env")

@dataclass
class Config:
    token: str = field(
        default_factory=lambda: CONFIG.get("TOKEN")
    )

    guild_id: int = field(
        default_factory=lambda: int(CONFIG.get("GUILD_ID"))
    )

    log_channel_id: int = field(
        default_factory=lambda: int(CONFIG.get("LOG_CHANNEL_ID"))
    )

    welcome_channel_id: int = field(
        default_factory=lambda: int(CONFIG.get("WELCOME_CHANNEL_ID"))
    )

    rules_channel_id: int = field(
        default_factory=lambda: int(CONFIG.get("RULES_CHANNEL_ID"))
    )

    plots_channel_id: int = field(
        default_factory=lambda: int(CONFIG.get("PLOTS_CHANNEL_ID"))
    )

    unverified_role_id: int = field(
        default_factory=lambda: int(CONFIG.get("UNVERIFIED_ROLE_ID"))
    )

    verified_role_id: int = field(
        default_factory=lambda: int(CONFIG.get("VERIFIED_ROLE_ID"))
    )

    vpn_role_id: int = field(
        default_factory=lambda: int(CONFIG.get("VPN_ROLE_ID"))
    )