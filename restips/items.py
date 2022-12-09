# Define here the models for your scraped items

import scrapy
from itemloaders.processors import TakeFirst , MapCompose, Join  #DataProcessing to get output in string insted of list #mapcompose to remove html_tag 
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
import re

def get_dm_1(Dm_1):
    if Dm_1:
        try:
            Dm_1 = Dm_1.split(',')[0]  
        except:
            Dm_1 = 'N/A'
    return Dm_1

def get_dm_2(Dm_2):
    if Dm_2:
        try:
            Dm_2 = Dm_2.split(',')[1]  
        except:
            Dm_2 = 'N/A'
    return Dm_2

def get_dm_3(Dm_3):
    if Dm_3:
        try:
            Dm_3 = Dm_3.split(',')[2]  
        except:
            Dm_3 = 'N/A'
    return Dm_3

def get_dm_4(Dm_4):
    if Dm_4:
        try:
            Dm_4 = Dm_4.split(',')[3]  
        except:
            Dm_4 = 'N/A'
    return Dm_4

def get_dm_5(Dm_5):
    if Dm_5:
        try:
            Dm_5 = Dm_5.split(',')[4]  
        except:
            Dm_5 = 'N/A'
    return Dm_5

def get_dm_6(Dm_6):
    if Dm_6:
        try:
            Dm_6 = Dm_6.split(',')[5]  
        except:
            Dm_6 = 'N/A'
    return Dm_6

def get_clean_website(value):
    if value is not None:
        list1 = []
        list1[:0] = value
        try:
            if (list1[-3] =='.') or (list1[-4] =='.'):
                new_value = ("".join(list1))
            else:
                new_value = 'N/A2'
        except IndexError:
            new_value = 'N/A'
    else:
        value = 'N/A'
        new_value = value
    return new_value

def get_clean_email(value):
    if '@' not in value:
        value = 'No @ sign'
    else:
        value = value.strip()        
    return value

def get_fax(value):
    if value is not None:
        value = value.replace('24hr', '').replace('24hrs', '').replace('24 hr', '').replace('24 hrs', '')
        value_1 = re.sub(r'[a-zA-Z]', r'', value)
        value_2 = value_1.replace('()', '').replace(':', '').replace('.', '')
    else:
        value_2 = 'N/A'
    return value_2

class RestipsItem(scrapy.Item):
    Link= scrapy.Field() 
    Name= scrapy.Field()
    Phone_1= scrapy.Field(
        input_processor = MapCompose(get_fax),
        output_processor = TakeFirst()
    )
    Phone_2 = scrapy.Field(
        input_processor = MapCompose(get_fax),
        output_processor = TakeFirst()
    )
    Fax = scrapy.Field(
        input_processor = MapCompose(get_fax),
        output_processor = TakeFirst()
    )
    Website = scrapy.Field(
        input_processor = MapCompose(get_clean_website),
        output_processor = TakeFirst()
    )
    Email = scrapy.Field(
        input_processor = MapCompose(get_clean_email),
        output_processor = TakeFirst()
    )
    Dm_1= scrapy.Field(
        input_processor = MapCompose(get_dm_1),
        output_processor = TakeFirst()
    )
    Dm_2= scrapy.Field(
        input_processor = MapCompose(get_dm_2),
        output_processor = TakeFirst()
    )
    Dm_3 = scrapy.Field(
        input_processor = MapCompose(get_dm_3),
        output_processor = TakeFirst()
    )
    Dm_4= scrapy.Field(
        input_processor = MapCompose(get_dm_4),
        output_processor = TakeFirst()
    )
    Dm_5= scrapy.Field(
        input_processor = MapCompose(get_dm_5),
        output_processor = TakeFirst()
    )
    Dm_6= scrapy.Field(
        input_processor = MapCompose(get_dm_6),
        output_processor = TakeFirst()
    )
    Published_date=scrapy.Field()
    Death_date= scrapy.Field()
    Funeral_director= scrapy.Field()
    Fd_address_1 = scrapy.Field()
    Fd_address_2= scrapy.Field()
    Fd_address_3 = scrapy.Field()
    Fd_address_4 = scrapy.Field()
