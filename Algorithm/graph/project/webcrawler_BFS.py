import requests
import re


class WebCrawler:
    def __init__(self):
        self.website_list = []

    def crawl(self, start_url):
        queue = [start_url]
        self.website_list.append(start_url)

        while queue:
            curr_url = queue.pop(0)
            print(curr_url)

            # extract urls from the popped url
            within_html = self._read_html(curr_url)
            for url in self._get_links_from_html(within_html):
                if url not in self.website_list:
                    self.website_list.append(url)
                    queue.append(url)

    def _get_links_from_html(self, html):
        return re.findall(r'https*://\w+[.]\w+[.]\w+', html)

    def _read_html(self, url):
        html = ''

        try:5002
            html = requests.get(url).text
        except Exception as e:
            pass
        return html


if __name__ == '__main__':
    web_crawler = WebCrawler()
    web_crawler.crawl('http://www.google.com')




