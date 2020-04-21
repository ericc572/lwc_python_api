from scrapy.exceptions import DropItem
import re

class CompanyPipeline(object):
    """ Raise Exception/DropItem if company does not match account"""

    def process_item(self, item, spider):
      # Gets Craigslist posting ID
      inputKeyword = spider.accountName.lower()
      scrapedKeyword = item['company'].lower()
      if inputKeyword != scrapedKeyword:
        if (inputKeyword not in scrapedKeyword) and (scrapedKeyword not in inputKeyword):
          raise DropItem('Dropping Item which has an invalid company name %s' % item)
      return item
