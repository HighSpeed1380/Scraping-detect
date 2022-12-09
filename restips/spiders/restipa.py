from datetime import datetime, timedelta
import scrapy
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from time import sleep
from random import randint
from ..items import RestipsItem
from scrapy.loader import ItemLoader

# start_input = input("input start date: ")
# print(start_input)  #dd_mm_yyyy

# start_input = start_inp

# end_input = input("input end date: ")
# print(end_input)    #dd_mm_yyyy

# county = input("input the county here: ")
# print(county)


class RestipSpider(scrapy.Spider):
    name = 'restipa'
    
    def start_requests(self):
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        option.add_argument("start-maximized")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
        
        driver.get("https://rip.ie/Deathnotices/Wicklow")
        driver.set_window_size(1920,1080)
        sleep(3)
        #input the start date 
        start_date = driver.find_element(By.XPATH, ('//div[@class="block5"]//input[@id="DateFrom"]'))
        start_date.clear()
        start_date.send_keys('04/05/2022') #start_input #dd_mm_yyyy # x replace it with yesterday's date
        # start_date.send_keys(Keys.ENTER)
        sleep(3)                    
        #input the end date
        end_date = driver.find_element(By.XPATH, ('//div[@class="block6"]//input[@id="DateTo"]'))
        end_date.clear()
        end_date.send_keys('05/05/2022')  #end_input #dd_mm_yyyy
        end_date.send_keys(Keys.ENTER)
        sleep(4)                
        
        links = []
        
        def get_sub_main():
            #---Getting links from the first page 
            def get_links():
                tb = driver.find_elements(By.XPATH, ('//tbody/tr/td/div/div/a'))
                for item in tb:
                    link = item.get_attribute('href')
                    links.append(link)
            get_links()
            try:
                next_page = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[not(contains(@class, 'disabled'))]//img[@class='next_ico spr_next_ico']")))
                if next_page:
                    next_page.click()                
                    sleep(4)
                    get_sub_main()
            except:
                pass
        
        get_sub_main()
        
        print(len(links))
        for index, ur in enumerate(links):
            print(f"we are currently at number {ur} page number{index}")
            yield scrapy.Request(url = ur, callback = self.parse_products_details, meta={'item_url':ur})

    def parse_products_details(self, response):
        games = response.xpath("//*[@class='left_dn']")
        for game in games:
            loader = ItemLoader(item=RestipsItem(), selector=game, response=response)
            loader.add_value("Link", response.meta['item_url']) 
            loader.add_xpath("Name", ".//li/a[@href='/Deathnotices/']/parent::li/following-sibling::li/text()")
            loader.add_xpath("Published_date", ".//div[contains(@class, 'dpubl')]/text()")
            loader.add_xpath("Death_date", ".//div[contains(@class, 'ddeath')]/text()")
            loader.add_xpath("Funeral_director", ".//*[@id='fun_info']/h4/text()")
            loader.add_xpath("Fd_address_1", "(.//*[@class='fd_address'])[1]/text()")
            loader.add_xpath("Fd_address_2", "(.//*[@class='fd_address'])[2]/text()")
            loader.add_xpath("Fd_address_3", ".//*[@class='fd_town']/text()")
            loader.add_xpath("Fd_address_4", ".//*[@class='fd_county']/text()")
            loader.add_xpath("Dm_1", ".//h3[@class='no-print']/span/text()")  
            loader.add_xpath("Dm_2", ".//h3[@class='no-print']/span/text()")
            loader.add_xpath("Dm_3", ".//h3[@class='no-print']/span/text()")
            loader.add_xpath("Dm_4", ".//h3[@class='no-print']/span/text()")
            loader.add_xpath("Dm_5", ".//h3[@class='no-print']/span/text()")
            loader.add_xpath("Dm_6", ".//h3[@class='no-print']/span/text()")
            loader.add_xpath("Phone_1", "(.//ul[@class='second_column']//img[@src='/img/ico_phone.png']/parent::div)[1]//text()")
            loader.add_xpath("Phone_2", "(.//ul[@class='second_column']//img[@src='/img/ico_phone.png']/parent::div)[2]//text()")
            loader.add_xpath("Fax", ".//ul[@class='second_column']//img[@src='/img/ico_fax.png']/parent::li//text()")
            loader.add_xpath("Website", ".//ul[@class='second_column']//img[@src='/img/ico_www.png']/parent::li//text()")
            loader.add_xpath("Email", ".//ul[@class='second_column']//img[@src='/img/ico_email.png']/parent::li//text()")
            
            yield loader.load_item()
  
  
  
  
                         
        
        

            