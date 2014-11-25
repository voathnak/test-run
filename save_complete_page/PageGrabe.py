__author__ = 'vlim'

import os
import requests
import BeautifulSoup

class PageGrabe(object):
    def __init__(self, domain, sub_root_dir, title, url):
        self.domain = domain
        self.sub_root_dir = sub_root_dir
        self.url = url
        self.title = title
        self.reguested = requests.get(url)
        self.directory = "%s%s" % (os.path.dirname(__file__), sub_root_dir)
        self.soup = BeautifulSoup(self.reguested.content)
    def save_all_link_tag(self):
        pass
    def grabe_link_tag(self, html_content):
        links = self.soup.find_all("link")

        print "##sub_root_dir: %s" % self.sub_root_dir

        for link in links:
            print link.get("href")

            link_content = requests.get('http://git-scm.com%s' % link.get("href"))

            complete_path = self.directory
            # Create dir before saving files to
            dir_split = link.get("href").split("/")
            dir_split = filter(bool, dir_split)
            print "##dir_split: %s" % dir_split
            # Remove file name from the dir path
            if len(dir_split) > 0:
                del dir_split[len(dir_split)-1]

                print "##dir_split: %s" % dir_split
                complete_path = "%s/%s" % (self.directory, "/".join(dir_split))
                print "##complete_path: %s" % complete_path
                print "##is exist: %s" % os.path.exists(complete_path)
                if not os.path.exists(complete_path):
                    os.makedirs(complete_path)

            with open('%s%s' % (self.directory, link.get("href")), 'w') as fid:
                fid.write(link_content.content)
            html_content= html_content.replace(link.get("href"), "%s%s%s" % (self.domain, self.sub_root_dir, link.get("href")))
        return html_content
    def create_required_dirs(self):
        pass
