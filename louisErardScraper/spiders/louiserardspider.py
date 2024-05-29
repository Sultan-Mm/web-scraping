import scrapy


class LouiserardspiderSpider(scrapy.Spider):
    name = "louiserardspider"
    allowed_domains = ["louiserard.com"]
    start_urls = ["https://louiserard.com/creations/?v=baa904278574&collection-first=excellence,heritage,la-sportive"]

    def parse(self, response):
        
        # Extracting watches from list of watches page
        watches = response.xpath('//*[@id="nm-shop-browse-wrap"]/ul/li')
        
        # Iterating through each watch in the list
        for watch in watches:
            
            name = watch.css('a ::attr(href)').get()
            
            # Check if the name contains "tyque", if so, skip to the next iteration. (tyque means the collections or bundle)
            if (name.find("tyque") == -1):
                watch_url = watch.css('a ::attr(href)').get()
                yield response.follow(watch_url, callback= self.parse_book_page)
            else:
                print('***continue***')
                continue
            
         # Extracting the URL of the next page for pagination
        next_page = response.css('div.nm-infload-link a ::attr(href)').get()
        if next_page is not None:
            next_page_url = next_page
            yield response.follow(next_page_url, callback= self.parse)

    
    # Extracting detailed information about the watch from its details page
    def parse_book_page(self, response):

        print('*********************************************')

         # Extracting the description of the watch, handling cases where it might be empty
        description = response.xpath('//div[@class="woocommerce-product-details__short-description entry-content"]/p/text()').extract()
        if len(description) == 0:
            # Using an alternative XPath for description if the initial one doesn't yield results
            description = response.xpath('//div[@class="woocommerce-product-details__short-description entry-content"]/p/strong/text()').extract()
            string_desc = "".join(description)
        else:
            string_desc = "".join(description)

        parent_model = response.xpath('//*[@id="nm-breadcrumb"]/a[3]/text()').get()
        title = response.xpath('//h1[@class="single-product-small-title"]/text()').get()

        # Extracting various details about the watch from its details page
        yield{
            'reference_number' : response.xpath('//div[@class="single-product-page-title"]/h2/text()').get(),
            'watch_URL' : response.url,
            'type' : response.xpath('//*[@id="tab-case_tab"]/div/div/div/div/div[1]/div[1]/p[2]/text()').get(),
            'brand' : 'Louis Erard',
            'year_introduced' : '',
            'parent_model' : response.xpath('//*[@id="nm-breadcrumb"]/a[3]/text()').get(),
            'specific_model' : parent_model +' '+ title,
            'nickname' : '',
            'marketing_name' : response.xpath('//div[@class="additional-features"]/text()').get(),
            'style' : '',
            'currency' : response.xpath('//p[@class="price"]//span[@class="woocommerce-Price-currencySymbol"]/text()').get(),
            'price' : response.xpath('//p[@class="price"]//bdi/text()').get(),
            'image_URL' : response.xpath('//div[@class="iconic-woothumbs-images-wrap"]//img/@src').get(),
            'made_in' : 'Switzerland',
            'case_shape' : '',
            'case_material' : response.xpath('//*[@id="tab-case_tab"]/div/div/div/div/div[1]/div[2]/p[2]/text()').get(),
            'case_finish' : '',
            'caseback' : response.xpath('//*[@id="tab-case_tab"]/div/div/div/div/div[1]/div[4]/p[2]/text()').get(),
            'diameter' : response.xpath('//*[@id="tab-case_tab"]/div/div/div/div/div[1]/div[3]/p[2]/text()').get(),
            'between_lugs' : response.xpath('substring-before(substring-after(//*[@id="tab-strap_tab"]/div/div/div/div/div[1]/div[3]/p[2]/text(), ""), ", ")').get(),
            'lug_to_lug' : '',
            'case_thickness' : '',
            'bezel_material' : '',
            'bezel_color' : '',
            'crystal' : response.xpath('//*[@id="tab-case_tab"]/div/div/div/div/div[1]/div[5]/p[2]/text()').get(),
            'water_resistance' : response.xpath('//*[@id="tab-case_tab"]/div/div/div/div/div[1]/div[6]/p[2]/text()').get(),
            'weight' : '',
            'dial_color' : response.xpath('//*[@id="tab-dial_tab"]/div/div/div/div/div[1]/div[1]/p[2]/text()').get(),
            'numerals' : '',
            'bracelet_material' : response.xpath('//*[@id="tab-strap_tab"]/div/div/div/div/div[1]/div[1]/p[2]/text()').get(),
            'bracelet_color' : response.xpath('//*[@id="tab-strap_tab"]/div/div/div/div/div[1]/div[1]/p[2]/text()').get(),
            'clasp_type' : response.xpath('//*[@id="tab-strap_tab"]/div/div/div/div/div[1]/div[2]/p[2]/text()').get(),
            'movement' : response.xpath('//*[@id="tab-movement_tab"]/div/div/div/div/div[1]/div[2]/p[2]/text()').get(),
            'caliber' : response.xpath('//*[@id="tab-movement_tab"]/div/div/div/div/div[1]/div[1]/p[2]/text()').get(),
            'power_reserve' : response.xpath('//*[@id="tab-movement_tab"]/div/div/div/div/div[1]/div[4]/p[2]/text()').get(),
            'frequency' : '',
            'jewels' : '',
            'features' : response.xpath('//*[@id="tab-movement_tab"]/div/div/div/div/div[1]/div[3]/p[2]/text()').get(),
            'description' : string_desc,
            'short_description' : '',
        }

