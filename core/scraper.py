import re
import urllib.request as urllib
import requests
from bs4 import BeautifulSoup


class Recent():

    def __init__(self):
        self.headers = {'user-agent': 'urmom'}
        self.url = requests.get("http://lupchan.org/recent.html",
                                headers=self.headers)
        self.soup = BeautifulSoup(self.url.text)
        self.rightbox = self.soup.find_all("div", {"class": "box right"})

    def getrecent(self):
        new = []
        rightlinks = []
        for x in self.rightbox:
            rightlinks += x.find_all("a")

        for x in rightlinks:
            new.append("http://lupchan.org" + x.get("href"))
        return new

    def getboard(self, url):
        url = urllib.urlopen(url).read()
        soup = BeautifulSoup(url)
        title = soup.find("title")
        return str(title)[7:-8]

    def getbody(self, url):
        tmp = url.split("#")
        url = requests.get(url, headers=self.headers).text
        text = re.sub("<br/>", " ", url)
        soup = BeautifulSoup(text)
        postnum = "reply_" + tmp[1]
        post = soup.find(id=postnum)

        if post is None:
            post = soup.find("div", {"class": "post op"})

        name = post.find("span", {"class": "name"}).get_text()
        datetime = post.find("time").get_text()
        tmp = post.find_all("a", {"class": "post_no"})
        postno = "No. " + tmp[1].get_text()
        body = post.find("div", {"class": "body"})
        return name, datetime, postno, body.get_text()
