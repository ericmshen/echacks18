api_key = "AIzaSyAUI7WLUEooG_7SpnIdPBm7mVIKzDyoV9U"
from apiclient.discovery import build

youtube = build('youtube', 'v3', developerKey=api_key)
print(type(youtube))
req = youtube.search().list(q='avengers', part='snippet', type='video', maxResults = 5)
print(type(req))
res = req.execute()

res['items'][0]
