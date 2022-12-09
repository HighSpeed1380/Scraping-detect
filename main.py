
from restips.spiders.restipa import RestipSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    process.crawl(RestipSpider)
    process.start()

if __name__ == '__main__':
    main()
    
#main function to run multiple spiders in a sequence 
#importing both spiders 

# from restips.spiders.restipa import RestipSpider
# from twisted.internet import reactor, defer
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.log import configure_logging
# from scrapy.utils.project import get_project_settings

# def main():
#     configure_logging()
#     settings = get_project_settings()
#     runner = CrawlerRunner(settings)

#     @defer.inlineCallbacks
#     def crawl():
#         yield runner.crawl(RestipSpider)           
#         reactor.stop()

#     crawl()
#     reactor.run() 
    
# if __name__=='__main__':
#     main()
    


