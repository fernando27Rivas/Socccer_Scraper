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


class ScraperSpider(CrawlSpider):
    name = 'scraper'
    allowed_domains = ['nursefly.com']
    search_url = 'https://nursefly.com'
    start_urls = ['https://nursefly.com']

    def parse(self, response):
        url = "https://nursefly.com"
        choice = settings.user
        choice2 = settings.pwd

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        #options.add_experimental_option("download.default_directory", "C:/Users/ferna/OneDrive/Desktop/Nursa_downloads")


        browser = webdriver.Chrome("C:/chromedriver.exe",chrome_options=options)

        browser.get(url)
        time.sleep(2)
        try:
            browser.find_element_by_xpath("//body/div/div/div/div/div[contains(@class, 'auth-section')]/button[2]").click()
            time.sleep(2)
        except NoSuchElementException:
            pass
            browser.find_element_by_xpath(
                "//body/div/div/div/div/div[contains(@class, 'auth-section')]/button[2]").click()
            time.sleep(2)
        try:
            browser.find_element_by_xpath("//body/div/div/div/div/div/div/div/button[2]").click()
            time.sleep(2)
        except NoSuchElementException:
            pass
            browser.find_element_by_xpath("//body/div/div/div/div/div/div/div/button[2]").click()
            time.sleep(2)
        try:
            browser.find_element_by_xpath("//body/div[@id='root']/div[@class='CoreLayout  sc-gzVnrw fpqIpg']/div[4]/div[2]/div[2]/div[@class='auth-popup-tabs QA__SignPopup']/div[3]/div[2]/div[@class='sign-up-popup-buttons']/button[@class='QA__LoginWithEmail--Button sc-bdVaJa eYqrwp']").click()

            time.sleep(2)
        except NoSuchElementException:
            pass
            browser.find_element_by_xpath(
                "//body/div/div/div/div/div/div/div/div[contains(@style, 'overflow: hidden')]/div[contains(@class, 'sign-up-popup-buttons')]/button[contains(@class, 'QA')]").click()
            time.sleep(2)
        try:
            user=browser.find_element_by_id('email')
            time.sleep(2)
        except NoSuchElementException:
            pass
            user = browser.find_element_by_id('email')
            time.sleep(2)

        try:
            user.send_keys(choice)
            time.sleep(2)
        except NoSuchElementException:
            pass
            user.send_keys(choice)
            time.sleep(2)
        try:
            pasw=browser.find_element_by_id('password')
            time.sleep(2)
        except NoSuchElementException:
            pass
            pasw = browser.find_element_by_id('password')
            time.sleep(2)
        try:
            pasw.send_keys(choice2)
            time.sleep(2)
        except NoSuchElementException:
            pass
            pasw.send_keys(choice2)
            time.sleep(2)
        try:
            browser.find_element_by_xpath("//button[@type='submit']").click()
        except NoSuchElementException:
            pass
            browser.find_element_by_xpath("//button[@type='submit']").click()

        time.sleep(10)

        try:
         browser.find_element_by_xpath("//body/div[@id='root']/div[@class='CoreLayout  sc-gzVnrw fpqIpg']/div[@class='global-header']/div[@class='main-header QA__DesktopHeader']/div[@class='auth-section']/div[@class='ProfileBadge']/div[@class='sc-bwzfXH mZRve']").click()
        except NoSuchElementException:
            pass
            time.sleep(2)
            browser.find_element_by_xpath("//body/div[@id='root']/div[@class='CoreLayout  sc-gzVnrw fpqIpg']/div[@class='global-header']/div[@class='main-header QA__DesktopHeader']/div[@class='auth-section']/div[@class='ProfileBadge']/div[@class='sc-bwzfXH mZRve']").click()
        try:
           time.sleep(10)
           browser.find_element_by_xpath("//body/div[9]/div/div/div/div/div/div[1]/span/div/div/div").click()
        except NoSuchElementException:
           pass
           time.sleep(10)
           browser.find_element_by_xpath("//body/div[9]/div/div/div/div/div/div[1]/span/div/div/div").click()

        try:
            time.sleep(5)
            browser.find_element_by_xpath("//tr/td[4]/a").click()
        except NoSuchElementException:
             pass
             time.sleep(2)
             browser.find_element_by_xpath("//tr/td[4]/a").click()

        try:
            time.sleep(4)
            var_len = browser.find_elements_by_xpath("//div/table/tbody/tr")
            description = []
            for result in var_len:
                description.append(result.text)
            #var_len=var_len.spli(sep='\n')
        except NoSuchElementException:
            pass
            time.sleep(2)
            var_len = browser.find_elements_by_xpath(
                "//div/table/tbody/tr")

            description = []
            for result in var_len:
                description.append(result.text)


        print("ESTE ES EL RESULTADO DE LA IMPRESION")
        print(description)
        print("AQUI :V")
        print("La cantidad de CV son: " +str( len(description)))
        i=1
        while(i<=len(description)):

            try:
                time.sleep(5)
                browser.find_element_by_xpath("//tr["+ str(i)+"]/td[6]/div/div/div").click()
            except NoSuchElementException:
                pass
                time.sleep(2)
                browser.find_element_by_xpath("//tr[" + str(i) + "]/td[6]/div/div/div").click()
            i=i+1

        browser.close()


