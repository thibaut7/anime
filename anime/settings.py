BOT_NAME = 'anime'

SPIDER_MODULES = ['anime.spiders']
NEWSPIDER_MODULE = 'anime.spiders'

# Basic settings
ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 1
DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = True
COOKIES_ENABLED = True

# Retry configuration
RETRY_ENABLED = True
RETRY_TIMES = 3
RETRY_HTTP_CODES = [403, 429, 500, 502, 503, 504]

# Default headers
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

# Middleware configuration
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
}

# Configure item pipelines
ITEM_PIPELINES = {
   'anime.pipelines.AnimePipeline': 300,
}

FEED_EXPORT_ENCODING = 'utf-8'

# Enable Scrapy's user agent middleware
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# Rotate User-Agent
# Install the 'scrapy-user-agents' package to enable User-Agent rotation:
# pip install scrapy-user-agents

# Enable IP rotation by setting up proxies (can use Scrapy's Proxy middleware or a custom proxy pool)
# Example: Using a custom list of proxies
PROXY_POOL_ENABLED = True

# Install the 'scrapy-proxy-pool' package:
# pip install scrapy-proxy-pool

# Respect the website's robots.txt (disable if it's an issue for scraping)

# Set download delay to avoid being flagged for aggressive scraping

# Enable retries for failed requests (useful for dealing with transient 403s)

# Disable cookies (to prevent server tracking in some cases)

# Enable HTTP caching to avoid making duplicate requests (optional)
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 3600  # Cache expiration time (in seconds)

# Set concurrent requests to a lower number to avoid being flagged as a bot
CONCURRENT_REQUESTS_PER_DOMAIN = 4
CONCURRENT_REQUESTS_PER_IP = 4

# Use a custom referrer to avoid blocking

# If CAPTCHA appears, use Scrapy Splash or Selenium for JavaScript-rendered content
# Splash settings (if needed for dynamic content)
# Install Splash and use the following configuration
# pip install scrapy-splash
SPLASH_URL = "http://localhost:8050"
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
