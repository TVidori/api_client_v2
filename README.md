# Api Client v2

This is a repository used for explaining how to create a custom API client using aiohttp and asyncio which handles credentials, sleep times and retries. 
The whole tutorial can be found at: https://medium.com/@thomas.vidori/66aca6027c6e

If you need to adapt the code for a different API, modify the `API_BASE_URL` constant in `src/currencyapi_client.py` then adjust the existing two endpoints functions (`print_latest_currency_exchange` and `get_currency_historical_exchange`) to your needs. 
You can also add more endpoints.

This client and the associated tutorial are based on a previous repository that can be found at: https://github.com/TVidori/api_client and a the associated tutorial at: https://medium.com/@thomas.vidori/d9863b3ae7c2.
