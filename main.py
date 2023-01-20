import time

import numpy
import pandas as pd
import asyncio
import aiohttp
from PIL import Image, UnidentifiedImageError
import io

from aiohttp import ClientPayloadError

file_data_frame = pd.read_excel("Parser_ImageSize.xlsx")
amount_of_links = file_data_frame.index.stop


async def get_size(response, index):
    try:
        data = await response.read()
        buff = io.BytesIO(data)
        size = Image.open(buff).size
        return f"{size[0]}x{size[1]}"
    except (UnidentifiedImageError, ClientPayloadError):
        file_data_frame.loc[index]["SIZE"] = "cannot identify image"


async def store_size(session, link, index):
    try:
        async with session.get(url=link) as response:
            size = await get_size(response, index)
            file_data_frame.loc[index]["SIZE"] = size
    except TypeError:
        file_data_frame.loc[index]["SIZE"] = numpy.NaN


async def main():
    async with aiohttp.ClientSession() as session:
        return await asyncio.gather(
            *[store_size(session=session,
                         link=file_data_frame.loc[index]["image_url"],
                         index=index
                         ) for index in range(0, amount_of_links-1)]
        )

if __name__ == '__main__':
    start = time.perf_counter()
    print("start")
    asyncio.run(main())
    file_data_frame.to_excel("Parser_ImageSize2.xlsx")
    end = time.perf_counter()
    print("Elapsed", end - start)
