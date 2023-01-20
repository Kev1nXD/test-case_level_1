import time

import asyncio
import aiohttp
from aiohttp import ClientSession, ClientResponse, ClientPayloadError
from PIL import Image, UnidentifiedImageError
import pandas as pd
import io

file_data_frame = pd.read_excel("Parser_ImageSize.xlsx")
amount_of_links = file_data_frame.index.stop


async def get_size(response: ClientResponse):
    try:
        data = await response.read()
        buff = io.BytesIO(data)
        size = Image.open(buff).size
        return f"{size[0]}x{size[1]}"
    except UnidentifiedImageError as e:
        print(f"{e}; image not found")


async def store_size(session: ClientSession, link: str, index: int):
    try:
        async with session.get(url=link) as response:
            size = await get_size(response)
            file_data_frame.loc[index]["SIZE"] = size
    except TypeError as e:
        print(f"{e}; URL is not valid")


async def main():
    try:
        async with aiohttp.ClientSession() as session:
            return await asyncio.gather(
                *[store_size(session=session,
                             link=file_data_frame.loc[index]["image_url"],
                             index=index
                             ) for index in range(0, amount_of_links)]
            )
    except ClientPayloadError as e:
        print(e)


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    file_data_frame.to_excel("Parser_ImageSize2.xlsx", sheet_name="Solution")
    end = time.perf_counter()
    print("Elapsed", end - start)
