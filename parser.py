import asyncio
from aiohttp import ClientSession, ClientResponse, ClientPayloadError
from PIL import Image, UnidentifiedImageError
from pandas import DataFrame
from io import BytesIO


class Sheet:
    def __init__(self, data_from_sheet: DataFrame):
        self.data_from_sheet = data_from_sheet


async def get_size(response: ClientResponse) -> str:
    """
    function is used to read the image from the response and return
    the size of the image in the format "width x height"

    :param response: response from page
    :return: size of image or "image not found" if page doesn't contain it
    """
    try:
        data = await response.read()
        buff = BytesIO(data)
        size = Image.open(buff).size
        return f"{size[0]}x{size[1]}"
    except UnidentifiedImageError as e:
        print(f"{e}; image not found")
        return "image not found"


async def store_size(
    session: ClientSession, link: str, index: int, data_to_parse: DataFrame
):
    """
    function is used to make a GET request to the link of the
    image, get the size of the image using 'get_size' function,
    and store the size in a new column of the DataFrame.

    :param session: client session
    :param link: link which should contain image
    :param index: index of dataframe row
    :param data_to_parse: DataFrame which contain links and where we should write image sizes
    """
    try:
        async with session.get(url=link) as response:
            size = await get_size(response)
            data_to_parse.loc[index]["SIZE"] = size
    except TypeError as e:
        print(f"{e}; URL is not valid")


async def parser(data_to_parse: DataFrame):
    """
    function is used to create a client session, make GET
    requests to all the links in the DataFrame using the store_size
    function, and gather all the results using 'asyncio.gather'

    :param data_to_parse: DataFrame which contain links and where we should write image sizes
    :return:
    """
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
