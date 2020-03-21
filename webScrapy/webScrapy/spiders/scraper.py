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
    allowed_domains = ['nursefly.com']
    search_url = 'https://nursefly.com'
    start_urls = ['https://nursefly.com']
     #sleep time
    short_sleep=4
    medium_sleep=5
    long_sleep=10


    def parse(self, response):
        url = "https://nursefly.com"
        choice = settings.user
        choice2 = settings.pwd
        chrome_options = webdriver.ChromeOptions()

   
        #the folder path of this .py file 
        current_directory=str(Path(__file__).parent.parent.absolute())
        #adding pdf for windows chrome path change only to "/pdf/" on linux
        path_dir=current_directory+'/pdf/'

        #defining the path when the data csv will be stored
        csv_dir=current_directory+"/data/"

        
        #creating the path on the OS
        Path(path_dir).mkdir(parents=True,exist_ok=True)
        Path(csv_dir).mkdir(parents=True,exist_ok=True)

        
        #avoid prompt severeal files downloaded and selecting the custom path for downloads
        prefs = {"download.default_directory": path_dir,"profile.default_content_setting_values.automatic_downloads": 1}#,"profile.managed_default_content_settings.images": 2}
            

        print(f"\033[94m  \033[0m")          
     
        #prefs = {"download.default_directory": path }
        chrome_options.add_experimental_option('prefs',prefs)
        #chrome_options.add_argument('--headless')
        #chrome_options.add_argument('window-size=1024x768')
        #chrome_options.add_argument("disable-gpu")
        #chrome_options.add_argument('--no-sandbox')
        #chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument("--start-maximized")
        #print(current_directory)

        #exec(open(current_directory+ '/'+'pdf_extraction.py').read())





        browser = webdriver.Chrome(settings.chromedriver_path,chrome_options=chrome_options)
        #browser.get('chrome://settings/')
        #browser.execute_script('chrome.settingsPrivate.setDefaultZoom(0.8);')
        #time.sleep(self.medium_sleep)

        if (self.file_exist(csv_path=csv_dir)):
            comparator_id=self.reader(csv_path=csv_dir)
        else:
            comparator_id=None


        browser.get(url)
        time.sleep(self.short_sleep)
        browser.get_cookies()

        # xpath to click sign in button
        try:
            browser.find_element_by_xpath("//div[contains(@class, 'auth-section')]/button[1]").click()
            time.sleep(self.short_sleep)

        except NoSuchElementException:
            pass
            browser.find_element_by_xpath("//div[contains(@class, 'auth-section')]/button[1]").click()
            time.sleep(self.short_sleep)



        #xpath to click login email
        try:
            user=browser.find_element_by_id("phoneOrEmailInput")
            user.send_keys(choice)
            time.sleep(self.short_sleep)
        except NoSuchElementException:
            pass
            user = browser.find_element_by_id("phoneOrEmailInput")
            user.send_keys(choice)
            time.sleep(self.short_sleep)
         #
        try:
            browser.find_element_by_xpath("//*[@id='root']/div/main/div[1]/div/div/form/button").click()
            time.sleep(self.short_sleep)
        except NoSuchElementException:
            pass
            browser.find_element_by_xpath("//*[@id='root']/div/main/div[1]/div/div/form/button").click()
            time.sleep(self.short_sleep)
        #fill login info    
        try:

            pasw = browser.find_element_by_id("password")
            pasw.send_keys(choice2)
            time.sleep(self.short_sleep)
        except NoSuchElementException:
            pass
            pasw = browser.find_element_by_id("password")
            pasw.send_keys(choice2)
            time.sleep(self.short_sleep)

        try:
            browser.find_element_by_xpath("//button[@type='submit']").click()
        except NoSuchElementException:
            pass
            browser.find_element_by_xpath("//button[@type='submit']").click()

        time.sleep(self.long_sleep)

        # redirect to dashboard url
        browser.get(url='https://www.nursefly.com/organization/48/admin')
        #select section to see pdf list
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

        print("La cantidad de CV son: " +str( len(var_len)))
        i=1
        #current pdfs
        current_pdfs=self.get_list_pdfs_downloaded(path_dir)

        element_ids=browser.find_element_by_xpath \
            ("//div/table/tbody/tr[1]/td[1]").text


        print("El ultimo ID es : " )
        print(element_ids)

        save_data=None
        if(comparator_id is not None):
            if (str(element_ids)== str(comparator_id)):
                print("Es el mismo ID no hay nuevos resultados")
                save_data=False
            else:
                print("Hay nuevos datos")
                save_data=True
        else:
            print("No hay registro previo se guardara todos los pdf")
            save_data=True



        count=0
        while(i<=len(var_len)):
            print(f"\033[94m Message: {i} \033[0m") 
            count=count+1
            nurse_name=self.get_actual_nurse(i,browser)
            element_id = browser.find_element_by_xpath \
                ("//div/table/tbody/tr["+ str(i) +"]/td[1]").text
            #if there's not name on pdf list it will be able to download a new pdf
            if( not(str(element_id)==str(comparator_id))):
                if(not nurse_name in current_pdfs):
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
            else:
                i=len(var_len)+1
            i=i+1
        #await for the last cv    
        time.sleep(self.long_sleep)
        self.clean_repeated_pdfs(path_dir)

        browser.close()
        print(f"\033[94m SCRIPT PDF \033[0m")
        print("Se descargaron "+ str(count) +" de la pagina Nursefly")


        if (save_data):
            self.write_csv(element_id=element_ids, csv_path=csv_dir)
            file_list = glob.glob(current_directory + "/pdf/*.pdf")

            file_list = [file_path.replace('\\', '/') for file_path in file_list]

            extract_data(file_list)




    def get_actual_nurse(self,index,browser):
        actual_nurse=browser.find_element_by_xpath(f"//tr[{index}]/td[2]").text #raw name from td
        actual_nurse=actual_nurse.lower().split(' ') #separate words between spaces
        separator='-' #separator
        actual_nurse=separator.join(actual_nurse)
        return actual_nurse


    def clean_repeated_pdfs(self,path):
        list_pdf = glob.glob(path+'/*.pdf')
        for pdf in list_pdf:
            if re.search(r'\([^)]*\)',pdf):
                os.remove(pdf)

    def has_any_download_active(self,temp_folder):
        chrome_temp_file = sorted(Path(temp_folder).glob('*.crdownload'))
        if(len(chrome_temp_file)>0):
            return True
        else:
            return False

    def get_list_pdfs_downloaded(self,temp_folder):
        list_pdf = glob.glob(temp_folder+'/*.pdf')
        list_pdf=[pdf_name.split('/')[-1] for pdf_name in list_pdf] #pdf with .pdf ended
        list_pdf=[pdf_name.split('-application.pdf')[0] for pdf_name in list_pdf] #pdf without pdf ended
        return list_pdf
        
    def write_csv(self,element_id,csv_path):
        print(element_id)
        print(csv_path)

        with open( csv_path +"data" + ".csv", "w") as csvFile:
            csv_output = csv.writer(csvFile)
            csv_output.writerow([element_id])

    def reader(self,csv_path):
        print(csv_path)
        final_id=None
        with open(csv_path+"data.csv") as csvFile:
            csv_output = csv.reader(csvFile)
            for row in csv_output:
                data = csv_output

                if(row is not None and   not (row==[])):
                    print("El Contenido del CSV es :")
                    print(row)
                    final_id=row[0]
        print("El valor del ID final es : " + final_id)
        return final_id

    def file_exist(self,csv_path):
        file = pathlib.Path( csv_path +"data.csv")

        if file.exists():
            print("File exist")
            return True
        else:
            print("File not exist")
            return False

                


