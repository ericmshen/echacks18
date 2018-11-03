api_key = "AIzaSyAUI7WLUEooG_7SpnIdPBm7mVIKzDyoV9U"

from datetime import datetime
from apiclient.discovery import build

youtube = build('youtube', 'v3', developerKey=api_key)
start_time = datetime(year=2005, month=1, day=1).strftime('%Y-%m-%dT%H:%M:%SZ')
end_time = datetime(year=2009, month=1, day=1).strftime('%Y-%m-%dT%H:%M:%SZ')

def get_channel_videos(channel_id):
    # get Uploads playlist id
    res = youtube.channels().list(id=channel_id,
                                  part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    videos = []
    next_page_token = None

    while 1:
        res = youtube.playlistItems().list(playlistId=playlist_id,
                                           part='snippet',
                                           maxResults=50,
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')

        if next_page_token is None:
            break
    return videos

def get_videos_stats(video_ids):
    stats = []
    for i in range(0, len(video_ids), 50):
        res = youtube.videos().list(id=','.join(video_ids[i:i+50]),
                                   part='statistics').execute()
        stats += res['items']

    return stats

#videos = get_channel_videos('UCkUq-s6z57uJFUFBvZIVTyg')
#video_ids = list(map(lambda x:x['snippet']['resourceId']['videoId'], videos))
#stats = get_videos_stats(video_ids)
#
#most_disliked = sorted(stats, key=lambda x:int(x['statistics']['dislikeCount']), reverse=True)
#
#for video in most_disliked:
#    print(video['id'], video['statistics']['dislikeCount'])

res = youtube.search().list(q='surfing',
                            part='snippet',
                            type='video',
                            maxResults = 20,
                            publishedAfter=start_time,
                            publishedBefore=end_time).execute()

#res = req.execute()

#for item in sorted(res['items'], key=lambda x:x['snippet']['publishedAt']):
#    print(item['snippet']['title'], item['snippet']['publishedAt'], item['id']['videoId'])

for item in res['items']:
    print(item['id']['videoId'])
