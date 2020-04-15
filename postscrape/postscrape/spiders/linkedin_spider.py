
from __future__ import print_function
import json
import re
import logging

import scrapy
from scrapy.http.request import Request
from postscrape.items import PostscrapeItem
# from spider_project.items import SpiderProjectItem

from six.moves.urllib import parse

class Linkedin_Site_Spider(scrapy.Spider):
    name = "linkedin_spider"

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
            descUrl = job.css('a.result-card__full-card-link::attr(href)').get()
            request = scrapy.Request(descUrl, callback=self.get_job_function)
            request.meta['item'] = item

            yield request

            if self.currentIndex < 25:
                next_link = response.url
                next_link = next_link[:next_link.find(self.accountName)] + self.accountName + '&start=' + str(25 * self.currentIndex)
                yield scrapy.Request(next_link, callback=self.parse)

            self.currentIndex += 1

    def get_job_function(self, response):
        item = response.meta['item']
        job_criteria_list = response.css('ul.job-criteria__list')
        item['category'] = job_criteria_list.css('span.job-criteria__text--criteria::text')[2].get()
        return item

