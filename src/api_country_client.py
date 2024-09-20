import aiohttp

API_BASE_URL = "https://api.country.is"


class ApiCountryClient:
    def __init__(self):
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=30),
        )

    async def close(self) -> None:
        await self.session.close()

    async def print_current_ip_and_its_country(self) -> None:
        response = await self.session.get(f"{API_BASE_URL}/")
        json = await response.json()
        print(json)

    async def get_ip_country(
            self,
            ip_address: str,
    ) -> str:
        response = await self.session.get(f"{API_BASE_URL}/{ip_address}")
        json = await response.json()

        return json["country"]
