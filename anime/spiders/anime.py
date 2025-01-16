import scrapy
from anime.items import AnimeItem

class AnimeSpider(scrapy.Spider):
    name = "animes"
    start_urls = [f"https://v6.voiranime.com/liste-danimes/page/{i}/" for i in range(1, 303)]

    def parse(self, response):
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
            item['Type'] = summary_contents[3].strip().replace("\n", "").replace("\t", "")
            item['status'] = summary_contents[4].strip().replace("\n", "").replace("\t", "")
            item['studio'] = summary_contents[5].strip().replace("\n", "").replace("\t", "")
            item['start_date'] = summary_contents[6].strip().replace("\n", "").replace("\t", "")
            item['genres'] = summary_contents[7].strip().replace("\n", "").replace
        summary_description = " ".join(summary_description).strip().replace("\n", "").replace("\t", "")
        item['rate'] = response.css("span#averagerate::text").get()
        item['total'] = response.css("span#countrate::text").get()
        item['summary_description'] = summary_description
        yield item
