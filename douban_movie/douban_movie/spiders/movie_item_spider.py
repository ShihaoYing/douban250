# -*- coding: utf-8 -*-

import scrapy
import numpy as np 
from douban_movie.items import DoubanMovieCommentItem, DoubanMovieItem, DoubanMovieUser
from urllib import parse as urlparse
from faker import Factory
from douban_movie.dns_cache import _setDNSCache

f = Factory.create()


class DoubanMovieSpider(scrapy.Spider):
    name = 'douban-movie'
    allowed_domains = ['accounts.douban.com', 'douban.com','movie.douban.com']
    start_urls = [
        'https://movie.douban.com/'
    ]




    def parse_movie(self, response):
        print(response.status)
        _setDNSCache()
        movie_item = DoubanMovieItem()
        # movie id
        movie_item['movie_id'] = response.xpath('.//li/span[@class='rec']/@id').extract()
        # movie title
        movie_item['movie_title'] = response.xpath('.//h1/span[@property="v:itemreviewed"]/text()').extract()
        # release date | year
        movie_item['release_date'] = response.xpath('.//h1/span[@class="year"]/text()').extract()
        # Director
        movie_item['directedBy'] = response.xpath('.//a[@rel='v:directedBy']/text()').extract()
        # Actors
        movie_item['starring'] = response.xpath('.//a[@rel='v:staring']/text').extract()
        # Genre
        movie_item['genre'] = response.xpath()