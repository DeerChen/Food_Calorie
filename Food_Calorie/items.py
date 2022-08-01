# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FoodCalorieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    food_cat = scrapy.Field()
    food_intro = scrapy.Field()  # 食物简介
    food_cal = scrapy.Field()  # 食物卡路里
    food_img_url = scrapy.Field()  # 食物示图
