from scrapy.exceptions import DropItem
import re

class CompanyPipeline(object):
    """ Raise Exception/DropItem if company does not match account"""

    def process_item(self, item, spider):
      # Gets Craigslist posting ID
      if item['company'] != spider.accountName:
        raise DropItem('Dropping Item which has an invalid company name %s' % item)
      return item
