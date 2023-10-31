BOT_NAME = "product_crawler"

SPIDER_MODULES = ["product_crawler.spiders"]
NEWSPIDER_MODULE = "product_crawler.spiders"

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

ROBOTSTXT_OBEY = False

DOWNLOAD_HANDLERS = {
    "http": "scrapy_zyte_api.ScrapyZyteAPIDownloadHandler",
    "https": "scrapy_zyte_api.ScrapyZyteAPIDownloadHandler",
}
DOWNLOADER_MIDDLEWARES = {
    "scrapy_zyte_api.ScrapyZyteAPIDownloaderMiddleware": 1000,
}
REQUEST_FINGERPRINTER_CLASS = "scrapy_zyte_api.ScrapyZyteAPIRequestFingerprinter"
ZYTE_API_KEY = "89a1b58a0c444ebabc8b69ef305cf78b"
ZYTE_API_TRANSPARENT_MODE = True

ITEM_PIPELINES = {
    "product_crawler.pipelines.DuplicatesPipeline": 100,
    # "product_crawler.pipelines.DatabasePipeline": 200,
}

FEED_EXPORT_FIELDS = ["product_id", "marketplace_id", "product_title", "title_desc", "product_price", "list_price", "manufacturer", "upc", "model_name", "product_dimensions", "product_weight", "customer_ratings", "average_rating", "listing_url", "image_url"]




#USER_AGENT = "product_crawler (+http://www.yourdomain.com)"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

#DOWNLOAD_DELAY = 3

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

#SPIDER_MIDDLEWARES = {
#    "product_crawler.middlewares.ProductCrawlerSpiderMiddleware": 543,
#}


#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}



#AUTOTHROTTLE_ENABLED = True

#AUTOTHROTTLE_START_DELAY = 5

#AUTOTHROTTLE_MAX_DELAY = 60
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
#AUTOTHROTTLE_DEBUG = False
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"


