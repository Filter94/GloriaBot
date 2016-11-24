#!/usr/bin/python
from apiclient.discovery import build

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
MAX_RESULTS = 10

DEVELOPER_KEY = ''
with file('youtube_api_key', 'r') as api_token_file:
    DEVELOPER_KEY = api_token_file.readline()
    api_token_file.close()


def youtube_search(keywords):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=keywords,
        part="id,snippet",
        maxResults=MAX_RESULTS
    ).execute()

    videos = []
    channels = []
    playlists = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    return search_response.get("items", [])
