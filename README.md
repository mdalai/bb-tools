# bb-tools
The tool is developed to make instructional design job easier and simple.  This tool is originally made for Blackboard. But feel free to utilize original codes for similar works. This tool is designed to work with HTML source code. 
## What is it for:
 - Remove messy SPAN tags that are auto-generated by the text editor; 
 - Embed Youtube Videos; 
 - Set the link to open in new window
 - Transform URL format into hyperlink

## Requirements:
- Install [python 2.7.13 64bit](https://www.python.org/downloads/release/python-2713/). Go to the link and choose "Windows x86-64 MSI installer".
- Install dependencies:
  * pip install python-qt5
  * pip install beautifulsoup4
- copy the github code to the local computer, either one of following should work:
  * download zip file
  * git clone
  
- Youtube API key
  * apply Google API key in [here](https://developers.google.com/youtube/v3/getting-started)
  * modify youtube_api.py, replace [YOUR-API-KEY] with the key you just applied.
## Guide:
Before using this tool, you have to get the html source code first. Otherwise, it won't work.

After your html code is ready, double click the 'bb_tools_UI.py', the following window should be openned:
![alt text](https://github.com/mdalai/bb-tools/blob/master/assets/htmlEdit.PNG "work window")

Then, we paste the HTML code into the first text box. Then, click the button looks like ![alt text](https://github.com/mdalai/bb-tools/blob/master/assets/btn.PNG "submit button"). A new html code will be generated in the second text box. You just need to copy all the new html code and paste it into the Blackboard. The new html code is generated solving three tasks mentioned in above. In the bottom, the code will also generate a description which includes how many SPAN tags are deleted, how many “Open to new Window: are handled and how many Youtube videos are embedded.


