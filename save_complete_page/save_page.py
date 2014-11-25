import urllib2
import re


page = urllib2.urlopen('http://stackoverflow.com')

page_content = page.read()

# links = re.findall(r"(href|src).*\".*(.css|.js|.ico|.jpg|.png).*\"", page_content)
# searhc_links = re.search(r"(href|src).*\".*(.css|.js|.ico|.jpg|.png).*\"", page_content)
# print type(links)
# print searhc_links.group()
related_file_name = {}
matches = re.finditer(r'(href|src).*\".*(.css|.js|.ico|.jpg|.png).*\"',page_content)
for match in matches:
    print match.group()


with open('page_content.html', 'w') as fid:
    fid.write(page_content)