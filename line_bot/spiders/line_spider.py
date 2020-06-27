import scrapy
import os.path
from line_bot.items import LineBotItem
from scrapy.loader import ItemLoader
import time



class NFLSpider(scrapy.Spider):
    name = 'nfl_spider'
    allowed_domains = ['sportsbookreview.com']
    start_urls = 'https://www.sportsbookreview.com/betting-odds/nfl-football/'

    def parse(self, response):

        # report which url scrapy is currently on
        self.logger.info('Parse function called on {}'.format(response.url))

        # Steal the actual html webpage for our record
        page = response.url.split("/")[-1]
        filename = 'sbr_lines/%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)



        # Collect the specific fields from each article
        loader = ItemLoader(item=LineBotItem(), response=response)
        loader.add_value('team', response.url.split("/")[3])
        loader.add_value('url', response.url)
        loader.add_xpath('date', '//div[@class="author-block__post-date"]/text()')
        loader.add_css('title', 'title::text')
        loader.add_xpath('tags', '//*[@class="tag__link"]/text()')
        loader.add_css('article', 'p')

        # load all items into scrapy
        item = loader.load_item()

        # I hate how the string outputs are in a list and I couldn't figure out why the ItemLoader made it that way 
        # this code overwrites the ItemLoader for a couple metrics to make they show up in the right order and format
        item['team'] = response.url.split("/")[3]
        item['url'] = response.url

        # Fin (French for Done and Done!)
        yield item