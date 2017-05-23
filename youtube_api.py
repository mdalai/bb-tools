import urllib, json

# check YOUTUBE videos with ID by Google YOUTUBE API
def youtubeChecker(youtube_id):
    try:
        urlAPI = "https://www.googleapis.com/youtube/v3/videos?part=status,snippet&id=%s&key=[YOUR-API-KEY]"%youtube_id
        response = urllib.urlopen(urlAPI)
        result = json.loads(response.read())
        if result["items"] == []:
            return None,None
        else:
            return result['items'][0]['status']['uploadStatus'],result['items'][0]['status']['embeddable'],result['items'][0]['snippet']['title']
    except:
        return 0,0,0
