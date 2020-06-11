# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
#from webScrapy.items import WebscrapyItem
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime,timedelta
import csv
from selenium.webdriver.support.ui import Select
from .. import settings
from selenium.common.exceptions import NoSuchElementException
from pathlib import Path
import pathlib
import os
import re
from ..pdf_extraction import extract_data
from scrapy.http import Request


#extract pdf functionality dependecies
from tika import parser
import glob
import csv

 
class ScraperSpider(CrawlSpider):
    name = 'scraper'
    allowed_domains = ['es.whoscored.com']
    search_url = 'https://es.whoscored.com/'
    start_urls = ['https://es.whoscored.com/']
     #sleep time
    short_sleep=4
    medium_sleep=5
    long_sleep=10


    def parse(self, response):
        url = "https://es.whoscored.com/"
        chrome_options = webdriver.ChromeOptions()
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--start-maximized")
        browser = webdriver.Chrome("C:/chromedriver", chrome_options=chrome_options)
        browser.get(url)
        time.sleep(10)

   

                


