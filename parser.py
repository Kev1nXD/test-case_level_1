import asyncio
from aiohttp import ClientSession, ClientResponse, ClientPayloadError
from PIL import Image, UnidentifiedImageError
from pandas import DataFrame
from io import BytesIO


class Sheet:
    def __init__(self, data_from_sheet: DataFrame):
        self.data_from_sheet = data_from_sheet


async def get_size(response: ClientResponse) -> str:
    try:
        data = await response.read()
        buff = BytesIO(data)
        size = Image.open(buff).size
        return f"{size[0]}x{size[1]}"
    except UnidentifiedImageError as e:
        print(f"{e}; image not found")
        return "image not found"


async def store_size(
    session: ClientSession,
        link: str,
        index: int,
        data_to_parse: DataFrame
):
    try:
        async with session.get(url=link) as response:
            size = await get_size(response)
            data_to_parse.loc[index]["SIZE"] = size
    except TypeError as e:
        print(f"{e}; URL is not valid")


async def parser(data_to_parse: DataFrame):
    try:
        async with ClientSession() as session:
            return await asyncio.gather(
                *[
                    store_size(
                        session=session,
                        link=data_to_parse.loc[index]["image_url"],
                        index=index,
                        data_to_parse=data_to_parse,
                    )
                    for index in range(0, len(data_to_parse))
                ]
            )
    except ClientPayloadError as e:
        print(e)


def parse_data(data_to_parse: DataFrame):
    sheet = Sheet(data_to_parse)
    asyncio.run(parser(data_to_parse=sheet.data_from_sheet))
    return sheet.data_from_sheet
