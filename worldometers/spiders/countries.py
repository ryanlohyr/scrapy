import scrapy


class CountriesSpider(scrapy.Spider):
    name = "countries" # Must be unique within a project
    allowed_domains = ["www.worldometers.info"] # never put http:// or https://
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        title = response.xpath("//h1/text()").get()
        countries = response.xpath("//td/a/text()").getall()
        
        yield {
            'title': title,
            'countries': countries
        }
