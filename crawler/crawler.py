import scrapy 

class MusicSpider(scrapy.Spider):
    name = 'music'
    start_urls = [
        'https://maistocadas.mus.br/1953/',
    ]

    def parse(self, response):
        for musicName in response.css('div.lista'): # Returns a selector 
            print(musicName)
            print("aaaa")            
#            yield {
#                'position' : musicname.xpath('ol@li').get(), 
                #'name': quote.xpath('span/small/text()').get(),
                #'text': quote.css('span.text::text').get(),
#            }
#        next_page = response.css('li.next a::attr("href")').get()
#        if next_page is not None:
#            yield response.follow(next_page, self.parse)