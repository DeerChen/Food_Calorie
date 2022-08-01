import re
import time

import requests
import scrapy
from bs4 import BeautifulSoup
from Food_Calorie.items import FoodCalorieItem


class BeveragesSpider(scrapy.Spider):
    name = "beverages"
    allowed_domains = ["food.hiyd.com"]
    start_urls = ["http://food.hiyd.com/"]

    def start_requests(self):
        url: str = "https://food.hiyd.com/list-6-html"
        response: requests.Response = requests.get(url)
        status_code: int = response.status_code
        if status_code == 200:
            soup: BeautifulSoup = BeautifulSoup(response.content, "lxml")
            number_pattern = re.compile(r"[0-9]+")
            page_count: int = int(
                re.findall(number_pattern, soup.find("ins").find("span").text)[0]
            )
            time.sleep(20)
            for index in range(page_count):
                yield scrapy.Request(
                    url="{}?page={}".format(url, index + 1), callback=self.parse
                )

        return []

    def parse(self, response):
        item: FoodCalorieItem = FoodCalorieItem()
        item["food_cat"] = response.xpath('//div[@class="box"]//h2/text()').get()

        cal_pattern = re.compile(r"热量：(.*)")

        lines = response.xpath('//div[@class="box"]//li')

        for li in lines:
            item["food_intro"] = li.xpath('*/div[@class="cont"]/h3/text()').get()

            item["food_cal"] = re.findall(
                cal_pattern, li.xpath('*/div[@class="cont"]/p/text()').get()
            )[0]

            item["food_img_url"] = li.xpath("*//img/@src").get()

            yield item
