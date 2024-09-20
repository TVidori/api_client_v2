import asyncio

from src.api_country_client import ApiCountryClient


async def call_api_country_endpoints() -> None:
    client = ApiCountryClient()
    await client.print_current_ip_and_its_country()
    country = await client.get_ip_country(
        ip_address="52.142.124.215",
    )
    print(country)

    await client.close()


if __name__ == "__main__":
    asyncio.run(call_api_country_endpoints())
