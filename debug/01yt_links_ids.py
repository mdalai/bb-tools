import re

txtHTML =''' 
<html><a href="https://www.youtube.com/watch?v=x2hF6AnVAio" >
<span><span>hello </span><span>OKKKK</span></span></a>
<a href="https://www.youtube.com/watch?v=1ZPCCmZ6-3E">abc</a>
<a href="https://www.youtube.com/watch?v=uv6ssCB03yw" target="_blank" width=1000>abc</a>
<a href="https://www.youtube.com/watch?v=diG519dFVNs">abc</a>
<a href="https://www.youtube.com/watch?v=v5_RwwecU4I">abc</a>
<a href="https://www.youtu.be/v/v5_RwwecU4I">abc</a>
<a href="https://www.gogole.be/v/v5_RwwecU4I">abc</a>
</html>
'''

txtHTML2 =''' 
<html><a href="https://www.youtube2222.com/watch?v=x2hF6AnVAio" >
<span><span>hello </span><span>OKKKK</span></span></a>
</html>
'''

# Messy html code for testing --------------
txtHTML1='''
<h4>ANNOTATED BIBLIOGRAPHIES</h4>
<p><em><strong>How to Prepare an Annotated Bibliography</strong></em><br /> <a target="_blank" href="http://olinuris.library.cornell.edu/ref/research/skill28.htm">http://olinuris.library.cornell.edu/ref/research/skill28.htm</a></p>
<p><em><strong>How to Write an Annotated Bibliography</strong></em><br /> <iframe width="560" height="315" src="//www.youtube.com/embed/Il_1Q3HZLhA" frameborder="0" allowfullscreen=""></iframe><br /> <a target="_blank" href=" https://www.youtube.com/watch?v=Il_1Q3HZLhA">https://www.youtube.com/watch?v=Il_1Q3HZLhA</a></p>
<p></p>
<p><em><strong>Writing an Annotated Bibliography Tutorial</strong></em><br /> <iframe width="560" height="315" src="//www.youtube.com/embed/5nW0swv5Mzs" frameborder="0" allowfullscreen=""></iframe><br /> <a target="_blank" href="https://www.youtube.com/watch?v=5nW0swv5Mzs">https://www.youtube.com/watch?v=5nW0swv5Mzs</a></p>
<h4>STYLE GUIDE AND FORMATTING REQUIREMENTS FOR ACADEMIC AND RESEARCH WRITING</h4>
<p><em><strong>APA Tutorial</strong></em><br /> This 30-45 minute tutorial from the American Psychological Association covers most of the important requirements of manuscript writing.<br /> All formal academic writing in the School of Education should be completed in APA format. Unless you are already very confident about writing in APA format, it is strongly suggested that you complete this tutorial (if you have not done so recently). Then submit all work using the appropriate APA formatting, especially as it relates to citations and the reference list.<br /> <a target="_blank" href="http://flash1r.apa.org/apastyle/basics/index.htm">http://flash1r.apa.org/apastyle/basics/index.htm</a></p>


<p><em style="margin: 0px; padding: 0px; border: 0px; outline: 0px; font-weight: normal; font-style: italic; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 13px; color: #000000; font-variant: normal; letter-spacing: normal; line-height: normal; orphans: auto; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 1; word-spacing: 0px; -webkit-text-stroke-width: 0px;"><strong style="margin: 0px; padding: 0px; border: 0px; outline: 0px; font-weight: bold; font-style: inherit; font-family: inherit; font-size: 13px;">UMUC Library: How to Write an Annotated Bibliography Tutorial</strong></em><br style="color: #000000; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 13px; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: auto; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 1; word-spacing: 0px; -webkit-text-stroke-width: 0px;" /><iframe width="560" height="315" style="border: 1px dotted #cc0000; cursor: default; margin: 0px; padding: 0px; outline: 0px; font-weight: normal; font-style: normal; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 13px; vertical-align: middle; max-width: 100%; height: auto; color: #000000; font-variant: normal; letter-spacing: normal; line-height: normal; orphans: auto; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 1; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-image: url('../../img/iframe.gif'); background-color: #ffffcc; background-position: 50% 50%; background-repeat: no-repeat;" src="//www.youtube.com/embed/RRPPoGsuOsg" frameborder="0" allowfullscreen=""></iframe><br style="color: #000000; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 13px; font-style: normal; font-variant: normal; font-weight: normal; letter-spacing: normal; line-height: normal; orphans: auto; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 1; word-spacing: 0px; -webkit-text-stroke-width: 0px;" /><a target="_blank" href="https://www.youtube.com/watch?v=RRPPoGsuOsg" style="margin: 0px; padding: 0px; border: 0px; outline: 0px; font-weight: normal; font-style: normal; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 13px; color: #00748b; text-decoration: underline; font-variant: normal; letter-spacing: normal; line-height: normal; orphans: auto; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 1; word-spacing: 0px; -webkit-text-stroke-width: 0px;">https://www.youtube.com/watch?v=RRPPoGsuOsg</a></p>
'''

#pattern = re.compile(r'(https?://)?(www\.)?(youtube|youtu)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
#pattern = re.compile(r'(https?://)?(www\.)?(youtube|youtu)(\.)(com|be)(/)(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
#pattern1 = re.compile(r'https?://www\.youtube|youtu)\.(com|be)/(watch\?v=|embed/|v/|.+\?v=)([^&=%\?]{11}))')
pattern = re.compile(r'(href=")(https?://)?(www\.)?(youtube|youtu)(\.)(com|be)(/)(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
Youtube_urls = re.findall(pattern,txtHTML)
#Youtube_urls2 = re.findall(pattern1,txtHTML)
#Youtube_urls2 = re.match(pattern1,txtHTML)

print Youtube_urls

#a = [(''.join(c),c[-1]) for c in Youtube_urls]
a = [(''.join(c[1:]),c[-1]) for c in Youtube_urls] # disinclude 'href="'
print a

b = [c[1] for c in a]
print b

for yt_url, yt_id in a:
    print yt_url, yt_id

print '<a href="%s'%yt_url

if txtHTML.find('<a href="%s'%yt_url,0)!= -1:
    print txtHTML.find('<a href="%s'%yt_url)


'''
#### Another way of getting Youtube ID
    # Extracting YOUTUBE_ID from URL -----------------------------
    def getYoutubeID(url):  
        if url.find("v=") != -1:
            start_pos = url.find("v=")+2
            end_pos = url.find("&", start_pos)
            if end_pos == -1:
                end_pos = url.find("#", start_pos)
                if end_pos == -1:
                    youtube_id = url[start_pos:]
                else:
                    youtube_id = url[start_pos:end_pos]
            else:
                youtube_id = url[start_pos:end_pos]
        elif url.find(".be/") != -1:
            start_pos = url.find(".be/")+4
            end_pos = url.find("?", start_pos)
            if end_pos == -1:
                youtube_id = url[start_pos:]
            else:
                youtube_id = url[start_pos:end_pos]

        else:
            youtube_id = 0

        return youtube_id
'''
