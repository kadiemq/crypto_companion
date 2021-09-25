from fetch_news import fetch_news
from save_news import save_news


def run_microservice():
    news = fetch_news()
    save_news(news)


if __name__ == '__main__':
    print('Starting news microservice')
    run_microservice()
