
from __future__ import print_function
import json
import re
import logging

import scrapy
from scrapy.http.request import Request
from postscrape.items import PostscrapeItem
from scrapy.http import Request, FormRequest
from scrapy.exceptions import CloseSpider

# from spider_project.items import SpiderProjectItem

from six.moves.urllib import parse

class Linkedin_Site_Spider(scrapy.Spider):
    name = "linkedin_spider"
    handle_httpstatus_list = [999]
    currentIndex = 0

    def __init__ (self, domain=None, accountName=""):
        self.accountName = accountName
        self.start_urls = [f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={accountName}"]

    def parse(self, response):
        jobDivs = response.css('li.result-card--with-hover-state')
        if (jobDivs and (response.status == 200)):
            for index, job in enumerate(jobDivs):
                item = PostscrapeItem()
                item['company'] = self.accountName
                item['title'] = job.css('h3.job-result-card__title::text').get()
                #item['company'] = job.css('a.job-result-card__subtitle-link::text').get()
                item['timeSincePost'] =  job.css('time::text').get()
                yield item

            next_link = response.url
            self.currentIndex += 1
            next_link = next_link[:next_link.find(self.accountName)] + self.accountName + '&start=' + str(25 * self.currentIndex)
            yield scrapy.Request(next_link, callback=self.parse)
