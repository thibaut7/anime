import scrapy
from anime.items import AnimeItem

class AnimeSpider(scrapy.Spider):
    name = "animes"
    base_url = "https://v6.voiranime.com/liste-danimes"
    start_urls = [base_url + "/"] + [f"https://v6.voiranime.com/liste-danimes/page/{i}/" for i in range(2, 303)]

    custom_settings = {
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://v6.voiranime.com/',
        }
    }

    def parse(self, response):
        # Vérification pour identifier un captcha
        if self.is_captcha_page(response):
            self.logger.warning("Captcha détecté. Résolution en cours...")
            yield scrapy.Request(
                url=response.url,
                callback=self.solve_captcha,
                dont_filter=True,
                meta={'captcha_response': response}
            )
        else:
            # Continuer à scraper les liens des animes
            for item in response.css("div.post-title.font-title a"):
                link = item.css("::attr(href)").get()
                if link:
                    yield response.follow(link, self.parse_details)

    def parse_details(self, response):
        item = AnimeItem()
        summary_contents = response.css("div.summary-content::text").getall()
        summary_description = response.css("div.summary-description p::text").getall()
        if len(summary_contents) >= 8:
            item['Native'] = summary_contents[0].strip().replace("\n", "").replace("\t", "")
            item['Romaji'] = summary_contents[1].strip().replace("\n", "").replace("\t", "")
            item['English'] = summary_contents[2].strip().replace("\n", "").replace("\t", "")
            item['Type'] = summary_contents[4].strip().replace("\n", "").replace("\t", "")
            item['Status'] = summary_contents[5].strip().replace("\n", "").replace("\t", "")
            item['Studios'] = summary_contents[6].strip().replace("\n", "").replace("\t", "")
            item['Start_date'] = summary_contents[7].strip().replace("\n", "").replace("\t", "")
            item['Genres'] = summary_contents[8].strip().replace("\n", "").replace("\t", "")
        summary_description = " ".join(summary_description).strip().replace("\n", "").replace("\t", "")
        item['Summary_description'] = summary_description
        item['Rate'] = response.css("span#averagerate::text").get()
        item['Total'] = response.css("span#countrate::text").get()
        yield item

    def is_captcha_page(self, response):
        """Détection de captcha (à adapter selon le site)."""
        return "captcha" in response.text.lower()

    def solve_captcha(self, response):
        """Passer la page captcha à un pipeline."""
        yield {
            'captcha_url': response.url,
            'captcha_response': response.meta.get('captcha_response')
        }
