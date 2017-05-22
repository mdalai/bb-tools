import sys
import urllib, json
import re
from bs4 import BeautifulSoup


# check YOUTUBE videos with ID by Google YOUTUBE API
def youtubeChecker(youtube_id):
    try:
        urlAPI = "https://www.googleapis.com/youtube/v3/videos?part=status&id=%s&key=AIzaSyAOBqTeqHaI1JTXzJNfQOzZZ-rMGmALHBw"%youtube_id
        response = urllib.urlopen(urlAPI)
        result = json.loads(response.read())
        if result["items"] == []:
            return None,None
        else:
            return result['items'][0]['status']['uploadStatus'],result['items'][0]['status']['embeddable']
    except:
        return 0,0

class htmlEdit(object):
    def __init__(self):
        pass
    def spanTagCleaner(self,htmlText):
        txt_HTML =htmlText.encode("utf-8")
        #txt_HTML =htmlText
        counter = 0
        while txt_HTML.find("<span>") != -1:
            span_start_pos = txt_HTML.find("<span>")
            span_close_start_pos = txt_HTML.find("</span>", span_start_pos)
            txt_HTML = txt_HTML[:span_start_pos] + txt_HTML[span_start_pos+6:span_close_start_pos] + txt_HTML[span_close_start_pos+7:]
            counter += 1

        return txt_HTML, counter

    def youtubeEmbeddedMaker(self,htmlText):
        # Get Youtube URLs and Youtube ID
        #pattern = re.compile(r'(https?://)?(www\.)?(youtube|youtu)(\.)(com|be)(/)(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
        #pattern = re.compile(r'(https?://)?(www\.)?(youtube|youtu)(\.)(com|be)(/)(watch\?v=|v/|.+\?v=)?([^&=%\?]{11})')
        pattern = re.compile(r'(href=")(https?://)?(www\.)?(youtube|youtu)(\.)(com|be)(/)(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
        yt_url_comp = re.findall(pattern,htmlText) # component
        #print yt_url_comp
        if yt_url_comp == []:
            return
        yt_urls = [(''.join(c[1:]),c[-1]) for c in yt_url_comp]
        #yt_urls = list(set(yt_urls))
        #print yt_urls

        counter = 0
        youtube_broken_links =[]
        youtube_notallow_embed =[]
        youtube_already_embed =[]
        start_pos = 0

        # Extract Youtube IDs from iFrames
        soup = BeautifulSoup(htmlText,"html.parser")
        ifr_yids =[ifr['src'][-11:] for ifr in soup.findAll('iframe') if ifr.has_attr('src') if re.search(re.compile('youtu'),ifr['src'])!=None]
        

        for yt_url, yt_id in yt_urls:

            # check YOUTUBE URL status
            uploadStatus,embeddable = youtubeChecker(yt_id)
            if uploadStatus == None or uploadStatus == 0:
                youtube_broken_links.append(yt_url)
                continue
            if uploadStatus == 'processed' and embeddable == False:
                youtube_notallow_embed.append(yt_url)
                continue

            # check if YOUTUBE URL is already embedded
            if yt_id in ifr_yids:
                youtube_already_embed.append(yt_url)
                continue

            htmlText = self.add_youtube_embed(htmlText,yt_url,yt_id)
            counter += 1
            print counter


        return htmlText, counter,youtube_notallow_embed, youtube_broken_links, youtube_already_embed

              
    def add_youtube_embed(self,htmlText,youtubeurl,youtubeid):
        pos = htmlText.find('<a href="%s'%youtubeurl) 
        add_iframe = '<br /><iframe width="560" height="315" src="https://www.youtube.com/embed/%s" frameborder="0" allowfullscreen=""></iframe>'%youtubeid
        txthtml = htmlText[:htmlText.find('</a>',pos) + 4] + add_iframe + htmlText[htmlText.find('</a>',pos) + 4:]      
        return txthtml


    def linkOpenNewTag(self, htmlText):
        txt_HTML =htmlText.encode("utf-8")
        counter = 0
        start_pos = 0
        
        while txt_HTML.find("<a ", start_pos)!= -1:
            a_tag_start_pos = txt_HTML.find("<a ", start_pos)
            a_tag_close_pos = txt_HTML.find(">", a_tag_start_pos)
            if txt_HTML.find("_blank", a_tag_start_pos, a_tag_close_pos) == -1:
                txt_HTML = txt_HTML.replace(txt_HTML[a_tag_start_pos:a_tag_close_pos+1],
                                 txt_HTML[a_tag_start_pos:a_tag_close_pos]+' target="_blank">',
                                 1)
                counter += 1
            #print txt_HTML 
            start_pos = a_tag_start_pos + 1

        return txt_HTML, counter




'''txtHTML = 
<html><a href="https://www.youtube.com/watch?v=x2hF6AnVAio" >
<span><span>hello </span><span>OKKKK</span></span></a>
<a href="https://www.youtube.com/watch?v=1ZPCCmZ6-3E">abc</a>
<a href="https://www.youtube.com/watch?v=uv6ssCB03yw" target="_blank" width=1000>abc</a>
<a href="https://www.youtube.com/watch?v=diG519dFVNs">abc</a>
<a href="https://www.youtube.com/watch?v=v5_RwwecU4I">abc</a>
</html>
'''
'''a = htmlEdit()
#txt, counter = a.spanTagCleaner(txtHTML)
#txt, counter = a.linkOpenNewTag(txtHTML)
txt, counter,youtube_notallow_embed,youtube_broken_links = a.youtubeEmbeddedMaker(txtHTML)
if youtube_notallow_embed:
    print "Following links are not allowed to embed: ", youtube_notallow_embed
if youtube_broken_links:
    print "Following YOUTUBE links are broken links: ", youtube_broken_links
print txt, counter
'''
