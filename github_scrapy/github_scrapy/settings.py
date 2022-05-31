BOT_NAME = 'github_scrapy'
SPIDER_MODULES = ['github_scrapy.spiders']
NEWSPIDER_MODULE = 'github_scrapy.spiders'
ITEM_PIPELINES = {
       'github_scrapy.pipelines.GithubScrapyPipeline': 300}
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "github_scrapy"
MONGODB_COLLECTION = "github_scrapy"
ROBOTSTXT_OBEY = True
