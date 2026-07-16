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
        default_factory=lambda: 1527063956407976087
    )

    log_channel_id: int = field(
        default_factory=lambda: 1527096735497719948
    )

    welcome_channel_id: int = field(
        default_factory=lambda: 1527114378749677608
    )

    rules_channel_id: int = field(
        default_factory=lambda: 1527103007794266263
    )

    plots_channel_id: int = field(
        default_factory=lambda: 1527095655527350342
    )

    unverified_role_id: int = field(
        default_factory=lambda: 1527071987917389894
    )

    verified_role_id: int = field(
        default_factory=lambda: 1527114285711360141
    )    