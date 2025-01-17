# settings.py
BOT_NAME = 'anime'

SPIDER_MODULES = ['anime.spiders']
NEWSPIDER_MODULE = 'anime.spiders'
# Nom de l'API Captcha
CAPTCHA_API_KEY = 'TON_API_KEY_2CAPTCHA'

# Activer les cookies
COOKIES_ENABLED = True

# User-Agent personnalisé
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'

# Respecter le fichier robots.txt
ROBOTSTXT_OBEY = False

# Délai entre les requêtes
DOWNLOAD_DELAY = 2
RANDOMIZE_DOWNLOAD_DELAY = True

# Activer le pipeline de captcha
ITEM_PIPELINES = {
    'anime.pipelines.CaptchaPipeline': 300,
}

# Activation des proxys rotatifs
DOWNLOADER_MIDDLEWARES = {
    'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
    'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
}

# ROTATING_PROXY_LIST = [
#     'https://147.75.34.92:9443',
#     'https://171.228.130.133:18589',
#     'http://41.207.187.178:80',
#     'http://203.170.66.154:8080',

#     #Ajoute plus de proxys ici
# ]

# Gestion des erreurs HTTP
RETRY_HTTP_CODES = [403, 429]
RETRY_TIMES = 5
