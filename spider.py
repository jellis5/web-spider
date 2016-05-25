import sys
import scrapy
import urllib.parse
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors import LinkExtractor

if len(sys.argv) != 2:
	print("Usage: python3.4 {} [website-url]".format(sys.argv[0]))
	sys.exit()
	
root_url = urllib.parse.urlsplit(sys.argv[1])

class MySpider(scrapy.Spider):
	name = "spider"
	custom_settings = {'AUTOTHROTTLE_ENABLED': True}
	allowed_domains = [root_url.hostname]
	start_urls = [root_url]
	start_urls = [sys.argv[1]]
	link_extract = LinkExtractor(allow_domains=root_url.hostname)
	links = set()

	def parse(self, response):
		for link in MySpider.link_extract.extract_links(response):
			MySpider.links.add(link.url)
			yield scrapy.Request(link.url, callback=self.parse, meta={'proxy': 'http://117.136.234.8:83'})

def main():
	process = CrawlerProcess()
	process.crawl(MySpider)
	process.start()
	for each in MySpider.links:
		print(each)
	
main()
