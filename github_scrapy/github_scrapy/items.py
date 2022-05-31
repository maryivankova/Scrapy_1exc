# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from scrapy.item import Item, Field


class GithubScrapyItem(Item):
    name_repository = Field()
    about = Field()
    url = Field()
    stars_num = Field()
    forks_num = Field()
    watching_num = Field()
    commits_num = Field()
    commit_last = Field()
    releases_num = Field()
    last_release = Field()
