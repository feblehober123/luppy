from core import scraper
from time import sleep


seenurls = []
while True:
    recent = scraper.Recent()
    urls = recent.getrecent()
    for url in urls:
        if url not in seenurls:
            seenurls.append(url)
            print(url)
            print(recent.getboard(url) + " " + " ".join(recent.getbody(url)))
    sleep(5)
