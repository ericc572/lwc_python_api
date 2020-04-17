from scrapy.exceptions import DropItem
import re

class CompanyPipeline(object):
    """ Raise Exception/DropItem if company does not match account"""

    def process_item(self, item, spider):
      # Gets Craigslist posting ID
      company = item['company'].lower()
      if not (company in spider.accountName or spider.accountName in company):
        raise DropItem('Dropping Item which has an invalid company name %s' % item)
      return item
