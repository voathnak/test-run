import urllib
import re
import sys
import os
page = urllib.urlopen("http://askubuntu.com/questions/350142/downloading-contents-of-the-web-page")
page = page.read()
fileHandle = open('content', 'w')
links = re.findall(r"<a.*?\s*href=\"(.*?)\".*?>(.*?)</a>", page)
for link in links:
    sys.stdout = fileHandle
    print ('%s' % (link[0]))
sys.stdout = sys.__stdout__
fileHandle.close() 
#os.system("grep -i '\/support\/security\/bulletins\/' content 2>/dev/null | head -n 3 | uniq | sed -e 's/^/http:\/\/www.adobe.com/g' > content1")
#os.system("wget -i content1")
