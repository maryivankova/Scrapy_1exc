
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class GithubScrapySpider(CrawlSpider):
    name = "github_scrapy"
    allowed_domains = ["github.com"]
    start_urls = [
        "https://github.com/scrapy",
        "https://github.com/celery"

    ]

    rules = (
    Rule(LinkExtractor(allow='scrapy'), callback='parse_rep'),
    Rule(LinkExtractor(allow='release')),
    Rule(LinkExtractor(allow='latest'), callback='parse_rel'),
    Rule(LinkExtractor(allow='celery'), callback='parse_rep'),
    Rule(LinkExtractor(allow='release')),
    Rule(LinkExtractor(allow='latest'),
                    callback='parse_rel')
    )

    def parse_rel(self, response):

        changelog_info = response.css('div.Box-body ::text').getall()
        return changelog_info

    def parse_rep(self, response):
        change_log = self.parse_rel(response)

        commit_tuple = [
                response.css('div.css-truncate a::text')[0:2].getall(),
                response.css
                ('a.Link--secondary relative-time::attr(datetime)').get(),
            ]

        commit_str = ', '.join(str(v) for v in commit_tuple)

        release_tuple = [
            response.css('a.Link--primary span.Counter::text').extract_first(),
            response.css
            ('div.text-small relative-time::attr(datetime)').getall(),
            response.css
            ('div.mt-3 a::attr(href)').extract_first(),
            change_log

        ]
        release_str = ', '.join(str(v) for v in release_tuple)

        yield{
            'name_repository': response.css('strong.mr-2 a::text').get(),
            'about': response.css('div.BorderGrid-cell p::text').get(),
            'url': response.css('strong.mr-2 a::attr(href)').get(),
            'stars_num': response.css('a.Link--muted strong::text').get(),
            'forks_num': response.css('a.Link--muted strong::text')[2:3].get(),
            'watching_num': response.css
            ('a.Link--muted strong::text')[1:2].get(),
            'commits_num': response.css('span.d-none strong::text').get(),
            'commit_last': commit_str,
            'releases_num': response.css
            ('a.Link--primary span.Counter::text').get(),
            'release_last': release_str,
            }
