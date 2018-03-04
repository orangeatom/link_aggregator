import pymongo
from urllib.parse import urlparse

from config import db

client = pymongo.MongoClient(db.host, db.port)


user_db = client.users


def check_message(text: str):
    splitted_text = text.split()
    url = urlparse(splitted_text[0])
    if urlparse(splitted_text[0]).netloc:
        print(url)
    pass


def _create_link(url, tags):
    pass


def _get_link_by_tags(tags):
    pass
