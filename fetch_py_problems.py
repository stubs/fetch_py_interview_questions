#! usr/bin/env python
import os
from bs4 import BeautifulSoup
import requests


def append_html(url):
    """Append html extension to a string url"""
    url += ".html"
    return url


def fetch_url(url_complete):
    """Request the url & return a text copy"""
    page_data = requests.get(url_complete).text
    return page_data


def bsoupify(page_data):
    """Pass raw page data through bs4 to extract all text"""
    page_text = BeautifulSoup(page_data, "lxml").get_text().encode("utf-8")
    return page_text


BASE_URL = "https://web.archive.org/web/20130502115734/http://www.streamtech.nl:80/problemset"
NEW_PATH = "./fetch_py_problems_output"

if not os.path.exists(NEW_PATH):
    os.makedirs(NEW_PATH)

for i in xrange(100, 200):
    sub_url = append_html(str(i))
    raw_page_html = fetch_url(BASE_URL+"/"+sub_url)
    bs_page_text = bsoupify(raw_page_html)
    with open(NEW_PATH + "/{}.txt".format(str(i)), "w") as out_file:
        out_file.write(bs_page_text)
