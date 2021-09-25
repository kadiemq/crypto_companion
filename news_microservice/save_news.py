from database_funcs import save_article_to_db


def save_news(data):
    data = data['value']

    for news in data:
        try:
            title = news['name']
            url = news['url']
            image = news['image']['contentUrl']

            save_article_to_db(title, url, image)

        except:
            print('Skipping No Image Found.')
