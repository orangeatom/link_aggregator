from lxml.html import fromstring

import requests
import pymongo

from config import db

client = pymongo.MongoClient(db.host, db.port)

collection = client.link_aggregator

user_db = collection.user
link_db = collection.link


class User:
    def __init__(self, user_id):
        self.user = user_db.find_one({"user_id": user_id})
        if not self.user:
            self.user = user_db.insert_one(
                {
                    "user_id": user_id,
                }
            )

        self.user_id = user_id
        self.chat_id = user_id

    def create_link(self, url, tags):
        content = requests.get(url).content
        title = fromstring(content).findtext(".//title").split("/")[0]
        print(title)
        if link_db.find_one({"url": url}):
            return self._update_tags_of_link(url, tags)
        else:
            link_db.insert_one(
                {
                    "user_id": self.user_id,
                    "url": url,
                    "tags": tags,
                    "title": title
                }
            )
            return "link created"

    def get_links_by_tags(self, tags):
        response = link_db.find(
            {
                'tags': {"$all": tags},
                "user_id": self.user_id
            })
        return response

    def delete_link(self, url):
        link = link_db.find_one_and_delete(
                {
                 "user_id": self.user_id,
                 "url": url
                }
            )
        if link:
            response = 'successful'
        else:
            response = "not found."
        return response

    def _update_tags_of_link(self, url, new_tags):
        link_db.find_one_and_update(
            {
                "url": url,
                "user_id": self.user_id,
            },
            {
               "$set": {"tags":  new_tags}
            }
            )
        return f"updated {new_tags}"
