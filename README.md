# Scrapy_1exc

***Requirements***


Python 3.6+

Scrapy > 1.6

Mongodb

**Install**

The quick way:

```
pip install scrapy
pip install pymongo
pip freeze > requirements.txt
```

***Specify Data***

The items.py file is used to define storage “containers” for the data that we plan to scrape.

The GithubScrapyIt() class inherits from Item (docs), which basically has a number of pre-defined objects that Scrapy has already built for us:

from scrapy.item import Item, Field


```
class GithubScrapyItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name_repository = Field()
    about = Field()
    url = Field()
    stars_num = Field()
    forks_num = Field()
    watching_num = Field()
    commits_num = Field()
    commit_last = Field()
    releases_num  = Field()
    last_release = Field()
  
```
**Create the Spider**
  
The first few variables are self-explanatory (docs):

>name defines the name of the Spider.
>allowed_domains contains the base-URLs for the allowed domains for the spider to crawl.
>start_urls is a list of URLs for the spider to start crawling from. 
All subsequent URLs will start from the data that the spider downloads from the URLS in start_urls.

> Rules tells the spider to follow all links with the allowed word.
What the spider does on the page is controlled by the 'callback'
   

    ```name = "github_scrapy"
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
    Rule(LinkExtractor(allow='latest'), callback='parse_rel')
    
    )```
    
 **Test**
 
  Again, run the following command within the “github_scrapy” directory:
  
   ```$ scrapy crawl guthub_scrapy ```
   
 **Import Data into Mongodb**
 
 You can use Mongodb Compass
 
 > Install Mongodb
 
 > Do connection
 
 ***Settings are in settings.py and pipelines.py directories*** 
 
 > Don't forget:
 > 
 ```sudo service mongod start```
 
   
    
    
