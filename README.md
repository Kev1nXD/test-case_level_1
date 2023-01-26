# Image Size Parser
## Description
The Image Size Parser is a Python script that asynchronously
parse image URLs from a Google Sheets document, and write it in a new Google sheet


## Usage
* Set the EMAIL_ADDRESS variable to email you want to get access to google sheet.

* Set the GOOGLE_SHEET_URL if you want to provide program your Google sheet.

* You also need to provide credentials.json file which contain your Google service accounts key 
here is an example:
```json
    {
  "type": "service_account",
  "project_id": "radiant-psyche-375512",
  "private_key_id": "794d9f****23c204253537b2178**9d3af9a1428b",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCYjKI4oc4h1QPx\neGDGqbf1eX3Cj8H5rfELkRxNGxvic/wN2FD31hxsPh7nb0HfdELOERPOuylfbnRX\n+9AKvv/UcaeUoOmdcOnVT6IWFu7TWSdLxSaE4tj5UV56ITdYi43mlgzBjySZ6YUx\nbUZwmGwcgav58pGkPqUV9ECm66S9Fjh9jDD4bNECdoPbgOUI7XBzVCBot/ek3S/4\ncHonlYTlfhqsDadxTw9gRPiAtFGApOGaQ93OHj2/rw2VqKQNtfqmNPjIOrYcy0aa\nT4aX8q5q66St5IThJ8B/t9aAIud8CnzROCvM1eht97bt6Puy2I9nfgoCaj/7roa8\nYfTBfZ15AgMBAAECggEABQ47qIWYQlGONy1mhI0xQbXjbemmhzu8dX70JRpBgUQJ\nUkN5m+poP0rEaqZVVJkZ1XXpwoat8CrF4/jMgIo5mGMXNb65BKMgK90X7FmZcE0e\nJY2ktqiaLJJpRqWrf2StfxBVNHKJgAyJkBrWgLqpx3WhXPG7NyMYkvZMl8ZA6CMP\n5WzO49+xqwkFF++kS4litJV2vwqyXEqAwDvkKNCsP0As0gA2aDH0NsQS+N0fKMDl\nb3bhkfsaAJAiRAa4r8l9HEUcXJCbaORFoEjfW2REnLlBriKoYpbCeV2tg3AidATg\nV5WhJsQ0yIwrFVnVRlCX/KoMd3klwDLtw4v2jng8rwKBgQDJ6QyMLwu/oNs7xH9s\n8ZVzaBTBGjljUdaWN/YrKMjdmAPN6lks25//REXg97rceas4RM6eJV4otjVEcQ96\nkprTP8lwIZLYD/GLUeYb7adFPHHnixBR5qFHSx+wjQ95JUIzDtsgZwM/4MrLzy8f\nGa4m48OmPa1FG+cdPCWnTxq98wKBgQDBamwbLOhfvFJ4eraBOyQL0fbJUg6LpJYF\nEwiATFe/o1b4gc3j1mVeHiZLOhjxynGzFlyrXBwycD773Z/XnWkq5iesQkAERZut\n30MAaPLs2/v602mRDZORoohyZ7oUybqlIVWrcLdVaZQv35Q1SDnzY937rtxHqauI\n0tizE1TV4wKBgBk3gvqrEYOQWnEffG6lyW2NbTIkzVALM4q1WIhRYqzSRH9eKl8A\n2v2tkDCln+/TPkAbz9ZOgnEBOKvglvdPAgkqKUVY3Bch/p/QzbVlPAPYpb0uUA56\niF/4EPAi3fDaZ2crDtEALJa4w3sq2A7BTU/MGG5Vu6Mq9fVfwrAfoA5jAoGAGomf\ni5r9xyTvq9gqclDLAVQtqDG6DS7n5opWAER5RbIDnNUyirA/+EnqtyehhItiTlAj\nJt/cfo8oFSazZ8IRS/GIP/pXDj7+vTyE1OmRay5DxIZ9VYmnVbQXRJs2zONg2Ida\nWct9XBrAWlEy5JykVuC89GtpjeuZvYwwb2GXokECgYB8HZeSK2zKFCVfE/c60fhK\nANDYyiS+hvUAafmfw5+AYlFrNLroc8Mw87XBjvTbtiRuctxJSU2ARG5qWkhm+Twx\nPVN4KEOfT8nlr++MpGnOcctU+UwMDKG8E99txXzgvkeUtH5Fihz/aJ0acbVtRsRF\ni7MzR8ut8MDavAIL4M4FGg==\n-----END PRIVATE KEY-----\n",
  "client_email": "***-****3@radiant-psyche-375512.iam.gserviceaccount.com",
  "client_id": "113069594847815442518",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/test-task3%40radiant-psyche-375512.iam.gserviceaccount.com"
}

```
