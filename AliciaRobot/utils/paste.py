from typing import List

from aiohttp import ClientSession


async def paste(content: str):
    """Paste the provided content to nekobin."""
    content = str(content)
    NEKOBIN_URL = "https://nekobin.com/"
    async with ClientSession() as sess:
        async with sess.post(
            NEKOBIN_URL + "api/documents",
            json={"content": content},
        ) as resp:
            if resp.status == 201:
                response = await resp.json()
                key = response["result"]["key"]
                final_url = f"{NEKOBIN_URL}{key}.txt"
                raw = f"{NEKOBIN_URL}raw/{key}.txt"
            else:
                raise Exception("Error Pasting to Nekobin")

    return final_url, raw