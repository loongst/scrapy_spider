# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter
class Js1Pipeline(object):

    def __init__(self):
        self.myfile=open("my3.json","wb")
        self.export=JsonLinesItemExporter(self.myfile,ensure_ascii=False,encoding="utf-8")

    def process_item(self, item, spider):
        self.export.export_item(item)

        self.myfile.close()
        return item

