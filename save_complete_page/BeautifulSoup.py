__author__ = 'vlim'
import httplib2
import requests
import os
from bs4 import BeautifulSoup, SoupStrainer

http = httplib2.Http()
status, response = http.request('http://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging')


# for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
#     if link.has_attr('href'):
#         print link['href']
r = requests.get('http://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging')
r2 = requests.get('http://git-scm.com/favicon.ico')
soup = BeautifulSoup(r.content)

domain = "http://test-run.dev/save_complete_page"
sub_root_dir = "/Git-Branching-Basic-Branching-and-Merging"
directory = "%s%s" % (os.path.dirname(__file__), sub_root_dir)
print "##directory: %s" % directory
if not os.path.exists(directory):
    os.makedirs(directory)

# with open('%s/favicon.ico' % directory, 'w') as fid:
#     fid.write(r2.content)



html_content = r.content


### GET ALL LINK TAG (css, ico)  ##################################
def get_all_link_tag(html_content):
    links = soup.find_all("link")

    print "##sub_root_dir: %s" % sub_root_dir

    for link in links:
        print link.get("href")

        link_content = requests.get('http://git-scm.com%s' % link.get("href"))

        complete_path = directory
        # Create dir before saving files to
        dir_split = link.get("href").split("/")
        dir_split = filter(bool, dir_split)
        print "##dir_split: %s" % dir_split
        # Remove file name from the dir path
        if len(dir_split) > 0:
            del dir_split[len(dir_split)-1]

            print "##dir_split: %s" % dir_split
            complete_path = "%s/%s" % (directory, "/".join(dir_split))
            print "##complete_path: %s" % complete_path
            print "##is exist: %s" % os.path.exists(complete_path)
            if not os.path.exists(complete_path):
                os.makedirs(complete_path)

        with open('%s%s' % (directory, link.get("href")), 'w') as fid:
            fid.write(link_content.content)
        html_content= html_content.replace(link.get("href"), "%s%s%s" % (domain, sub_root_dir, link.get("href")))
    return html_content
#+++++++++++++++++++++++++++++++++++++++++++++++++++++#


html_content = get_all_link_tag(html_content)



### GET ALL IMG TAG  ##################################

imgs = soup.find_all("img")


with open('%s/%s.html' % (directory, "Git-Branching-Basic-Branching-and-Merging"), 'w') as fid:
    fid.write(html_content)


