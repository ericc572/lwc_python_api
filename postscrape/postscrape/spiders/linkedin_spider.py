
from __future__ import print_function
import json
import re
import logging

import scrapy
from scrapy.http.request import Request
from postscrape.items import PostscrapeItem
from scrapy.http import Request, FormRequest
# from spider_project.items import SpiderProjectItem

from six.moves.urllib import parse

class Linkedin_Site_Spider(scrapy.Spider):
    name = "linkedin_spider"
    handle_httpstatus_list = [999]


    def __init__ (self, domain=None, accountName=""):
        self.accountName = accountName
        self.start_urls = [f"https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords={accountName}"]
        self.currentIndex = 1

    def parse(self, response):
        jobDivs = response.css('li.result-card--with-hover-state')
        for index, job in enumerate(jobDivs):
            item = PostscrapeItem()
            item['title'] = job.css('h3.job-result-card__title::text').get()
            item['company'] = job.css('a.job-result-card__subtitle-link::text').get()
            item['timeSincePost'] =  job.css('time::text').get()

            yield item

            if self.currentIndex < 25:
                next_link = response.url
                next_link = next_link[:next_link.find(self.accountName)] + self.accountName + '&start=' + str(25 * self.currentIndex)
                yield scrapy.Request(next_link, callback=self.parse)

            self.currentIndex += 1
