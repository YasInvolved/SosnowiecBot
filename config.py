import os
from dataclasses import dataclass, field
from dotenv import load_dotenv

load_dotenv()

@dataclass
class Config:
    token: str = field(
        default_factory=lambda: os.environ.get("TOKEN")
    )

    guild_id: int = field(
        default_factory=lambda: int(os.environ.get("GUILD_ID"))
    )

    log_channel_id: int = field(
        default_factory=lambda: int(os.environ.get("LOG_CHANNEL_ID"))
    )

    welcome_channel_id: int = field(
        default_factory=lambda: int(os.environ.get("WELCOME_CHANNEL_ID"))
    )

    rules_channel_id: int = field(
        default_factory=lambda: int(os.environ.get("RULES_CHANNEL_ID"))
    )

    plots_channel_id: int = field(
        default_factory=lambda: int(os.environ.get("PLOTS_CHANNEL_ID"))
    )

    unverified_role_id: int = field(
        default_factory=lambda: int(os.environ.get("UNVERIFIED_ROLE_ID"))
    )

    verified_role_id: int = field(
        default_factory=lambda: int(os.environ.get("VERIFIED_ROLE_ID"))
    )

    vpn_role_id: int = field(
        default_factory=lambda: int(os.environ.get("VPN_ROLE_ID"))
    )