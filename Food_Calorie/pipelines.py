# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymongo


class FoodCaloriePipeline:
    def __init__(self):
        client = pymongo.MongoClient(host="localhost", port=27017)
        self.db = client["食物卡路里"]

    def process_item(self, item, spider):
        food_cat = item["food_cat"]
        self.db[food_cat].insert_one(dict(item))
        return item
