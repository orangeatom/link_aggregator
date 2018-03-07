import pymongo
from urllib.parse import urlparse

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
        link_db.insert_one(
            {
                "user_id": self.user_id,
                "url": url,
                "tags": tags
            }
        )
        pass
    
    def get_links_by_tags(self, tags):
        response = link_db.find(
            {
                'tags': {"$all": tags},
                "user_id": self.user_id
            })

    def delete_link(self, url):
        l = link_db.find_one_and_delete(
                {
                "user_id": self.user_id,
                 "url": url
                }
            )
        if l:
            response = 'successful'
        else:
            response = "not found."
        return response

    def update_tags_of_link(self, url, new_tags):
        link = link_db.find_one_and_update(
            {
                "user_id": self.user_id,
                "tags": {"$all": new_tags}
                }
            )
        return link

