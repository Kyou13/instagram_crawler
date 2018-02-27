import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_splash import SplashRequest
from ..items import MapionspiderItem

class MapionSpider(CrawlSpider):
    name = 'Mapion_spider'
    allowed_domains = ['mapion.co.jp']

    # 引数でジャンル、カテゴリー、チェーン店のID情報を受け取る。
    def __init__(self, genre=None, category=None, chain_store=None, *args, **kwargs):
        super(MapionSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['http://www.mapion.co.jp/phonebook/{0}{1}{2}/'.format(genre,category,chain_store)]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse_item, args={'wait': 0.5}, )

    def parse_item(self, response):
        item = MapionspiderItem()
        shop_info = response.xpath('//*[@id="content"]/section/table/tbody')
        if shop_info:
            item['name'] = shop_info.xpath('tr[1]/td/text()').extract()
            url_path = shop_info.xpath('//a[@id="spotLargMap"]/@href').extract()
            # 店舗の地図情報(url_path)から緯度経度情報を抜き出し、list型にしてitemに渡します。
            url_elements = url_path[0].split(',')
            item['latitude'] = [url_elements[0][4:]]
            item['longitude'] = [url_elements[1]]
            yield item

        # 店舗一覧から各店舗詳細のlink先を取得する。
        list_size = len(response.xpath('//table[@class="list-table"]/tbody/tr').extract())
        for i in range(2,list_size+1):
            target_url_path = '//table[@class="list-table"]/tbody/tr['+str(i)+']/th/a/@href'
            target = response.xpath(target_url_path)
            if target:
                target_url = response.urljoin(target[0].extract())
                yield SplashRequest(target_url, self.parse_item)

        # 店舗一覧の下部にある次のページ番号のlink先を取得する。
        next_path = response.xpath('//p[@class="pagination"]/*[contains(@class, "pagination-currnet ")]/following::a[1]/@href')
        if next_path:
            next_url = response.urljoin(next_path[0].extract())
            yield SplashRequest(next_url, self.parse_item)
