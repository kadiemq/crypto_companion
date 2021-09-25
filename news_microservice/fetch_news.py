import http.client
import json

from config import headers

url = 'bing-news-search1.p.rapidapi.com'


def fetch_news():
    connection = http.client.HTTPSConnection(url)
    connection.request("GET", "/news/search?q=btc&safeSearch=Off&textFormat=Raw&originalImg=true&freshness=Day",
                       headers=headers)

    res = connection.getresponse()
    data = res.read()
    data = data.decode('utf-8')
    data = json.loads(data)

    return data
