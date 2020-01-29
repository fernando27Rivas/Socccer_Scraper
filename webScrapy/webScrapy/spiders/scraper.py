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
import os
from scrapy.http import Request

#extract pdf functionality dependecies
from tika import parser
import glob
import csv

class ScraperSpider(CrawlSpider):
    name = 'scraper'
    allowed_domains = ['nursefly.com']
    search_url = 'https://nursefly.com'
    start_urls = ['https://nursefly.com']
     #sleep time
    short_sleep=2
    medium_sleep=4
    long_sleep=10
    def parse(self, response):
        url = "https://nursefly.com"
        choice = settings.user
        choice2 = settings.pwd
        chrome_options = webdriver.ChromeOptions()

   

        #the folder path of this .py file 
        current_directory=str(Path().absolute())
        #adding pdf for windows chrome path change only to "/pdf/" on linux
        pdf_directories=current_directory+'\\pdf\\'
        #defining the path when the data csv will be stored
        csv_dir=current_directory+"/data/"
        #naming a timestamp folder for pdf-cv downloaded at certain date
        directory_name=str(datetime.now().strftime('cv-downloaded-%Y-%m-%d-%H-%M-%S'))
        #joning strings to get the path_dir where pdf files will be stored
        path_dir=pdf_directories+directory_name
        #creating the path on the OS
        Path(path_dir).mkdir(parents=True,exist_ok=True)
        #avoid prompt severeal files downloaded and selecting the custom path for downloads
        prefs = {"download.default_directory": path_dir,"profile.default_content_setting_values.automatic_downloads": 1}#,"profile.managed_default_content_settings.images": 2}


        
     
        #prefs = {"download.default_directory": path }
        chrome_options.add_experimental_option('prefs',prefs)
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('window-size=1920x1080')
        chrome_options.add_argument("disable-gpu")
        #chrome_options.add_argument('--no-sandbox')
        #chrome_options.add_argument('--disable-dev-shm-usage')

        #chrome_options.add_argument("--start-maximized")
        #options.add_experimental_option("download.default_directory", "C:/Users/ferna/OneDrive/Desktop/Nursa_downloads")


        browser = webdriver.Chrome("C:/chromedriver.exe",chrome_options=chrome_options)

        browser.get(url)
        time.sleep(self.short_sleep)
        browser.get_cookies()

        try:
            browser.find_element_by_xpath("//body/div/div/div/div/div[contains(@class, 'auth-section')]/button[2]").click()
            time.sleep(self.short_sleep)
        except NoSuchElementException:
            pass
            browser.find_element_by_xpath(
                "//body/div/div/div/div/div[contains(@class, 'auth-section')]/button[2]").click()
            time.sleep(self.short_sleep)
        try:
            browser.find_element_by_xpath("//body/div/div/div/div/div/div/div/button[2]").click()
            time.sleep(self.short_sleep)
        except NoSuchElementException:
            pass
            browser.find_element_by_xpath("//body/div/div/div/div/div/div/div/button[2]").click()
            time.sleep(self.short_sleep)
        try:
            browser.find_element_by_xpath("//body/div[@id='root']/div[@class='CoreLayout  sc-gzVnrw fpqIpg']/div[4]/div[2]/div[2]/div[@class='auth-popup-tabs QA__SignPopup']/div[3]/div[2]/div[@class='sign-up-popup-buttons']/button[@class='QA__LoginWithEmail--Button sc-bdVaJa eYqrwp']").click()

            time.sleep(self.short_sleep)
        except NoSuchElementException:
            pass
            browser.find_element_by_xpath(
                "//body/div/div/div/div/div/div/div/div[contains(@style, 'overflow: hidden')]/div[contains(@class, 'sign-up-popup-buttons')]/button[contains(@class, 'QA')]").click()
            time.sleep(self.short_sleep)
        try:
            user=browser.find_element_by_id('email')
            time.sleep(self.short_sleep)
        except NoSuchElementException:
            pass
            user = browser.find_element_by_id('email')
            time.sleep(self.short_sleep)

        try:
            user.send_keys(choice)
            time.sleep(self.short_sleep)
        except NoSuchElementException:
            pass
            user.send_keys(choice)
            time.sleep(self.short_sleep)
        try:
            pasw=browser.find_element_by_id('password')
            time.sleep(self.short_sleep)
        except NoSuchElementException:
            pass
            pasw = browser.find_element_by_id('password')
            time.sleep(self.short_sleep)
        try:
            pasw.send_keys(choice2)
            time.sleep(self.short_sleep)
        except NoSuchElementException:
            pass
            pasw.send_keys(choice2)
            time.sleep(self.short_sleep)
        try:
            browser.find_element_by_xpath("//button[@type='submit']").click()
        except NoSuchElementException:
            pass
            browser.find_element_by_xpath("//button[@type='submit']").click()

        time.sleep(self.long_sleep)

        # try:
        #  browser.find_element_by_xpath("//body/div[@id='root']/div[@class='CoreLayout  sc-gzVnrw fpqIpg']/div[@class='global-header']/div[@class='main-header QA__DesktopHeader']/div[@class='auth-section']/div[@class='ProfileBadge']/div[@class='sc-bwzfXH mZRve']").click()
        # except NoSuchElementException:
        #     pass
        #     time.sleep(self.short_sleep)
        #     browser.find_element_by_xpath("//body/div[@id='root']/div[@class='CoreLayout  sc-gzVnrw fpqIpg']/div[@class='global-header']/div[@class='main-header QA__DesktopHeader']/div[@class='auth-section']/div[@class='ProfileBadge']/div[@class='sc-bwzfXH mZRve']").click()
        # try:
        #    time.sleep(self.long_sleep)
        #    browser.find_element_by_xpath("//body/div[9]/div/div/div/div/div/div[1]/span/div/div/div").click()
        # except NoSuchElementException:
        #    pass
        #    time.sleep(self.long_sleep)
        #    browser.find_element_by_xpath("//body/div[9]/div/div/div/div/div/div[1]/span/div/div/div").click()
        browser.get(url='https://www.nursefly.com/organization/48/admin')

        try:
            time.sleep(self.medium_sleep)
            browser.find_element_by_xpath("//tr/td[4]/a").click()
        except NoSuchElementException:
             pass
             time.sleep(self.short_sleep)
             browser.find_element_by_xpath("//tr/td[4]/a").click()

        try:
            time.sleep(self.medium_sleep)
            var_len = browser.find_elements_by_xpath("//div/table/tbody/tr")
        except NoSuchElementException:
            pass
            time.sleep(self.short_sleep)
            var_len = browser.find_elements_by_xpath("//div/table/tbody/tr")

        print("AQUI :V")
        print("La cantidad de CV son: " +str( len(var_len)))
        i=1
        while(i<=len(var_len)):
            print(f"\033[94m Message: {i} \033[0m")   

            try:
                time.sleep(self.medium_sleep)
                browser.find_element_by_xpath("//tr["+ str(i)+"]/td[6]/div/div/div[1]").click()
            except NoSuchElementException:
                pass
                time.sleep(self.long_sleep)
                browser.find_element_by_xpath("//tr[" + str(i) + "]/td[6]/div/div/div[1]").click()
            #wait for iterate another time until pdf get downloaded
            time.sleep(3)
            while self.has_any_download_active(path_dir):
                time.sleep(1)
            i=i+1
        #await for the last cv    
        time.sleep(self.long_sleep)
        
        browser.close()
        print(f"\033[94m SCRIPT PDF \033[0m")   
        self.extractPdfData(pdf_path=path_dir,csv_path=csv_dir)




    def has_any_download_active(self,temp_folder):
        chrome_temp_file = sorted(Path(temp_folder).glob('*.crdownload'))
        if(len(chrome_temp_file)>0):
            return True
        else:
            return False

    def extractPdfData(self,pdf_path,csv_path):
        file_list=glob.glob(pdf_path+"/*.pdf")
        file_list=[file_path.replace('pdf\\','pdf/') for file_path in file_list]

        #in case at least one pdf exists, the csv timestamp name will be created 
        if(file_list):
            file_csv_name=datetime.now().strftime('nursefly-%Y-%m-%d-%H-%M-%S.csv')
            with open(csv_path+file_csv_name, "w+") as file_output:
                csv_output = csv.writer(file_output)
                csv_output.writerow(["Name", "Phone","Email","Address","SSN","Date of Birth","Speciality","Travel Experience"])

        #the csv listed ordered by datetime of creation    
        csv_list=glob.glob(csv_path+"/*.csv")
        csv_list=[file_path.replace('data\\','data/') for file_path in csv_list]
        self.logger.error(csv_list)
        for file_path in file_list:
            raw = parser.from_file(file_path)
            #focused on content
            raw = str(raw['content'])
            raw_lines=raw.splitlines()

            #here the data will be filter avoiding empty strings
            data= list(filter(None,raw_lines))
            #get personal data
            #get personal data
            name=data[0]
            if("PHONE" in data):
                phone_index=data.index("PHONE")+1
                phone=data[phone_index]
            else:
                phone="Phone not Avaible"

            if("EMAIL" in data):
                email_index=data.index("EMAIL")+1
                email=data[email_index]
            else:
                email="Email not Avaible"

            if("ADDRESS" in data):
                address_start_index=data.index("ADDRESS")+1
                address_end_index=data.index("SSN")
                address=" ".join(data[address_start_index:address_end_index])
            else:
                address="Address not Avaible"

            if("SSN" in data):
                ssn_index= data.index("SSN")+1
                ssn=data[ssn_index]
                if(ssn == "DATE OF BIRTH"):
                    ssn="SSN not Avaible"
            else:
                ssn="SSN not Avaible"
                
            if("DATE OF BIRTH" in data):
                birth_index=data.index("DATE OF BIRTH")+1
                birth=data[birth_index]
                if(birth == "HIGHLIGHTS"):
                    birth="Date not Avaible"
            else:
                birth="Date not Avaible"

            if("SPECIALTY" in data):
                speciality_start_index=data.index("SPECIALTY")+1

                if("TRAVEL EXPERIENCE" in data):
                    speciality_end_index=data.index("TRAVEL EXPERIENCE")
                elif("LICENSES" in data):
                    speciality_end_index=data.index("LICENSES")
                

                
                speciality=" ".join(data[speciality_start_index:speciality_end_index])
            else:
                speciality="Specialty not Avaible"
            
            if("TRAVEL EXPERIENCE" in data):
                travel_experience=True
            else:
                travel_experience=False
            name=data[0]
            if("PHONE" in data):
                phone_index=data.index("PHONE")+1
                phone=data[phone_index]
            else:
                phone="Phone not Avaible"

            if("EMAIL" in data):
                email_index=data.index("EMAIL")+1
                email=data[email_index]
            else:
                email="Email not Avaible"

            if("ADDRESS" in data):
                address_start_index=data.index("ADDRESS")+1
                address_end_index=data.index("SSN")
                address=" ".join(data[address_start_index:address_end_index])
            else:
                address="Address not Avaible"

            if("SSN" in data):
                ssn_index= data.index("SSN")+1
                ssn=data[ssn_index]
                if(ssn == "DATE OF BIRTH"):
                    ssn="SSN not Avaible"
            else:
                ssn="SSN not Avaible"
                
            if("DATE OF BIRTH" in data):
                birth_index=data.index("DATE OF BIRTH")+1
                birth=data[birth_index]
                if(birth == "HIGHLIGHTS"):
                    birth="Date not Avaible"
            else:
                birth="Date not Avaible"

            if("SPECIALTY" in data):
                speciality_start_index=data.index("SPECIALTY")+1

                if("TRAVEL EXPERIENCE" in data):
                    speciality_end_index=data.index("TRAVEL EXPERIENCE")
                elif("LICENSES" in data):
                    speciality_end_index=data.index("LICENSES")
                

                
                speciality=" ".join(data[speciality_start_index:speciality_end_index])
            else:
                speciality="Specialty not Avaible"
            
            if("TRAVEL EXPERIENCE" in data):
                travel_experience=True
            else:
                travel_experience=False           


            with open(csv_list[-1], "a") as file_output:
                csv_output = csv.writer(file_output)
                csv_output.writerow([name, phone,email,address,ssn,birth,speciality,travel_experience])
                


