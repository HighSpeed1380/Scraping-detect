# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from itemadapter import ItemAdapter

class RestipsPipeline:
    def process_item(self, item, spider):
        return item


# settings.py


# import mysql.connector

# class RestipsPipeline:

#     def __init__(self):
#         self.conn = mysql.connector.connect(
#             host = 'localhost',
#             user = 'root',
#             password = 'za********34',
#             database = 'rest_in_peace'
#         )

#         ## Create cursor, used to execute commands
#         self.cur = self.conn.cursor()
        
#         ## Create quotes table if none exists         # CREATE DATABASE IF NOT EXISTS rest_kro_6;  USE rest_kro_6;
#         self.cur.execute("""
#         CREATE TABLE IF NOT EXISTS sample_table_3(
#             id int NOT NULL auto_increment, 
#             Link VARCHAR(255),
#             Name VARCHAR(255),
#             Phone_1 VARCHAR(255),
#             Phone_2 VARCHAR(255),
#             Fax VARCHAR(255),
#             Website VARCHAR(255),
#             Email VARCHAR(255),
#             Dm_1 VARCHAR(255),
#             Dm_2 VARCHAR(255),
#             Dm_3 VARCHAR(255),
#             Dm_4 VARCHAR(255),
#             Dm_5 VARCHAR(255),
#             Dm_6 VARCHAR(255),
#             Published_date VARCHAR(255),
#             Death_date VARCHAR(255),
#             Funeral_director VARCHAR(255),
#             Fd_address_1 VARCHAR(255),
#             Fd_address_2 VARCHAR(255),
#             Fd_address_3 VARCHAR(255),
#             Fd_address_4 VARCHAR(255),
#             PRIMARY KEY (id)
#         )
#         """)

#     def process_item(self, item, spider):   
#         ## Define insert statement
#         self.cur.execute("""insert into sample_table_3 (Link, Name, Phone_1, Phone_2, Fax, Website, Email, Dm_1, Dm_2, Dm_3, Dm_4, Dm_5, Dm_6, Published_date, Death_date, Funeral_director, Fd_address_1, Fd_address_2, Fd_address_3, Fd_address_4)
#                          values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (
#             item["Link"],
#             item["Name"],
#             item["Phone_1"],
#             item["Phone_2"],
#             item["Fax"],
#             item["Website"],
#             item["Email"],
#             item["Dm_1"],
#             item["Dm_2"],
#             item["Dm_3"],
#             item["Dm_4"],
#             item["Dm_5"],
#             item["Dm_6"],
#             item['Published_date'], 
#             item['Death_date'],
#             item['Funeral_director'],         
#             item['Fd_address_1'],
#             item['Fd_address_2'],
#             item['Fd_address_3'],
#             item['Fd_address_4']
#         ))
        
#         ## Execute insert of data into database
#         self.conn.commit()
    
#     def close_spider(self, spider):

#         ## Close cursor & connection to database 
#         self.cur.close()
#         self.conn.close()