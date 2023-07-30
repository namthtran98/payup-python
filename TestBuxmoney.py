from Buxmoney import Buxmoney
import threading
import concurrent.futures
from selenium import webdriver
from joblib import Parallel, delayed
from concurrent import futures
import wd.parallel
import unittest

# t1 = Parallel(n_jobs=2)(delayed(Buxmoney(buxusername="awsnamtran02@gmail.com",buxpassword="Sinhnam1998", apikey="o8EPL80Zhhp0RX7eu4fcYkVxoL5nci42")))
# t2 = Parallel(n_jobs=2)(delayed(Buxmoney(buxusername="awsnamtran02@gmail.com",
#                                         buxpassword="Sinhnam1998", apikey="o8EPL80Zhhp0RX7eu4fcYkVxoL5nci42")))


class ScrapeThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url

    def run(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        page_source = driver.page_source
        driver.close()
        # do something with the page source


urls = [
    'https://en.wikipedia.org/wiki/0',
    'https://en.wikipedia.org/wiki/1',
    'https://en.wikipedia.org/wiki/2',
    'https://en.wikipedia.org/wiki/3',
]

threads = []
for url in urls:
    t = ScrapeThread(url)
    t.start()
    threads.append(t)

for t in threads:
    t.join()
