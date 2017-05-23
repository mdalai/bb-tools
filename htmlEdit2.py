import sys
import urllib, json
import re
from bs4 import BeautifulSoup
import youtube_api


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
        # Get Youtube URLs and Youtube ID from tag A
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

        # URL to hyperlink counter
        counter2 = 0

        # Extract Youtube IDs from iFrames
        soup = BeautifulSoup(htmlText,"html.parser")
        ifr_yids =[ifr['src'][-11:] for ifr in soup.findAll('iframe') if ifr.has_attr('src') if re.search(re.compile('youtu'),ifr['src'])!=None]


        # Get Youtube URLs FROM text of tag A
        pattern2 = re.compile(r'(>)(https?://)?(www\.)?(youtube|youtu)(\.)(com|be)(/)(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
        yt_url_txt = re.findall(pattern2,htmlText) # component
        #print yt_url_txt
        yt_urls_txt = [''.join(c[1:]) for c in yt_url_txt]
        #print yt_urls_txt
        

        for yt_url, yt_id in yt_urls:

            # check YOUTUBE URL status
            uploadStatus,embeddable,title = youtube_api.youtubeChecker(yt_id)
            if uploadStatus == None or uploadStatus == 0:
                youtube_broken_links.append(yt_url)
                continue
            if uploadStatus == 'processed' and embeddable == False:
                youtube_notallow_embed.append(yt_url)
                continue

            # URL to hyperlink
            if yt_url in yt_urls_txt:
                htmlText = self.url2hyperlink(htmlText,yt_url,title)
            counter2 += 1
            #print counter2
            #print title

            # check if YOUTUBE URL is already embedded
            if yt_id in ifr_yids:
                youtube_already_embed.append(yt_url)
                continue

            htmlText = self.add_youtube_embed(htmlText,yt_url,yt_id)
            counter += 1
            #print counter

            


        return htmlText, counter,youtube_notallow_embed, youtube_broken_links, youtube_already_embed, counter2

              
    def add_youtube_embed(self,htmlText,youtubeurl,youtubeid):
        pos = htmlText.find('<a href="%s'%youtubeurl) 
        add_iframe = '<br /><iframe width="560" height="315" src="https://www.youtube.com/embed/%s" frameborder="0" allowfullscreen=""></iframe>'%youtubeid
        txthtml = htmlText[:htmlText.find('</a>',pos) + 4] + add_iframe + htmlText[htmlText.find('</a>',pos) + 4:]      
        return txthtml

    def url2hyperlink(self,htmlText,youtubeurl,title):
        pos = htmlText.find('>%s'%youtubeurl)
        txthtml = htmlText[:pos+1] + "Youtube:"+ title + htmlText[pos+1+len(youtubeurl):]      
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



