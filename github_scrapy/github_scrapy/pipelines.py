import pymongo

class GithubScrapyPipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )

        db = self.conn['mycrapys']
        self.collection = db['github_scrapy']

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
