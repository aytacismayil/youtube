import requests
from googleapiclient.discovery import build
api_key="AIzaSyAA1MwJpEpCZbET5XndDFDZTCIKJAadowg"
youtube=build("youtube","v3",developerKey=api_key)
results = youtube.search().list(part='snippet',
order='viewCount',
type='video',
maxResults=10)
response = results.execute()
for i in response["items"]:
    print(i["snippet"]["title"])