import asyncio

from src.currencyapi_client import CurrencyApiClient


async def call_currencyapi_client_endpoints() -> None:
    client = CurrencyApiClient()
    await client.print_latest_currency_exchange()
    euros_value = await client.get_currency_historical_exchange(
        date="2022-01-01",
        currency="EUR"
    )
    print(euros_value)

    await client.close()


if __name__ == "__main__":
    asyncio.run(call_currencyapi_client_endpoints())
