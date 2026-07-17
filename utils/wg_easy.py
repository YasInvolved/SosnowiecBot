import aiohttp
import io
from dotenv import dotenv_values
from typing import Dict, Any, Optional

_CONFIG = dotenv_values(".env")

class WgEasyAdapter:
    def __init__(self):
        self.base_url: str = _CONFIG.get("WG_EASY_URL")
        self.username: str = _CONFIG.get("WG_EASY_USERNAME")
        self.password: str = _CONFIG.get("WG_EASY_PASSWORD")

        self._session: Optional[aiohttp.ClientSession] = None
    
    async def __aenter__(self):
        self._session = aiohttp.ClientSession(self.base_url)
        await self._login(self._session)
        return self
    
    async def __aexit__(self, exc_type, exc, tb):
        if self._session:
            await self._session.close()

    async def _login(self, session: aiohttp.ClientSession):
        payload = { "username": self.username, "password": self.password, "remember": False }
        async with session.post("/api/session", json=payload) as response:
            data: Dict[str, Any] = await response.json()
            if response.status != 200:
                raise RuntimeError(f"Authentication failed with status: {response.status} {data}")
            
            if str(data.get("status")).lower() != "success":
                raise RuntimeError(f"Authentication rejected by server: {data}")
            
    async def create_client(self, name: str) -> str:
        payload = {"name": name, "expiresAt": None }

        async with self._session.post("/api/client", json=payload) as response:
            if response.status != 200:
                raise RuntimeError(f"Failed to create client '{name}: {response.status}'")
            
            data: Dict[str, Any] = await response.json()
            return data["clientId"]
        
    async def get_client_config_stream(self, client_id: str) -> io.BytesIO:
        url = f"/api/client/{client_id}/configuration"

        async with self._session.get(url) as response:
            if response.status != 200:
                raise RuntimeError(f"Failed to fetch config for ID {client_id}: {response.status}")
            
            raw_bytes = await response.read()
            return io.BytesIO(raw_bytes)

    