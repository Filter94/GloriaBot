#!/usr/bin/python
from apiclient.discovery import build

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
MAX_QUERY_RESULTS = 50
MAX_VIDEOS_RESULTS = 10

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
        maxResults=MAX_QUERY_RESULTS
    ).execute()

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    videos_only_entities = filter(lambda entry: entry["id"]["kind"] == "youtube#video",
                                  search_response.get("items", []))
    videos = map(lambda x: x["id"]["videoId"], videos_only_entities)
    return videos[:MAX_VIDEOS_RESULTS]
