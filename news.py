# the following is my key of the api News page:
# Api Key: fdf5ea1549a7403ab38313aa4322c801

import requests
# from pprint import pprint

class NewsEmail:

    base_url = "https://newsapi.org/v2/everything?"
    api_key = "fdf5ea1549a7403ab38313aa4322c801"

    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)

        email_body = ''
        for article in articles:
            email_body = email_body + "\n" + article['title'] + "\n" + article['url'] + "\n\n"
            # this simbol (\n) is a brakeline to separate among the pther items that I want to separe.

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content["articles"]
        return articles

    def _build_url(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"
        return url


if __name__ == "__main__":
    send_to_email = NewsEmail(interest='Billionaire', from_date='2022-12-25', to_date='2023-1-23', language='en')
    print(send_to_email.get())
