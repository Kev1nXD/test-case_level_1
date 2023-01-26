import time

import gspread
import gspread_dataframe as gd
from google.oauth2.service_account import Credentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas

from parser import parse_data

EMAIL_ADDRESS = "example@gmail.com"

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)
google_auth = GoogleAuth()
drive = GoogleDrive(google_auth)

if __name__ == "__main__":
    start = time.perf_counter()
    sheet_data = client.open_by_url(
        "https://docs.google.com/spreadsheets/d/1QX2IhFyYmGDFMvovw2WFz3wAT4piAZ_8hi5Lzp7LjV0/edit#gid=1902149593"
    ).get_worksheet(0)
    data = pandas.DataFrame(sheet_data.get_all_records())
    worksheet = client.create("Solution")
    worksheet.share(EMAIL_ADDRESS, perm_type="user", role="writer", notify=False)
    gd.set_with_dataframe(worksheet.get_worksheet(0), parse_data(data_to_parse=data))
    end = time.perf_counter()
    print("Elapsed", end - start)
    print(worksheet.url)
