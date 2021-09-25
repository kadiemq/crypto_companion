import psycopg2

from config import user, password, host, database

conn = psycopg2.connect(user=user,
                        password=password,
                        host=host,
                        database=database)


def already_inserted(title):
    cur = conn.cursor()

    cur.execute(f"select * from news_model where title = '{title}'")
    count = cur.rowcount

    if count == 0:
        return False
    else:
        cur.close()
        conn.close()
        return True


def save_article_to_db(title, url, img_url):
    if already_inserted(title):
        return

    cur = conn.cursor()

    cur.execute(f"insert into news_model (title, image, url) VALUES ('{title}', '{img_url}', '{url}')")
    conn.commit()
    cur.close()
    conn.close()
    print('saved article to db')
