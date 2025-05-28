from atproto import Client
from dotenv import load_dotenv
from typing import Any
import os

load_dotenv()

handle = os.getenv('BSKY_HANDLE')
password = os.getenv('BSKY_APP_PASSWORD')

class BlueskyBot:
    def __init__(self, handle: str, app_password: str):
        self.client = Client()
        self.client.login(handle, app_password)

    def post_message(self, content: str):
        self.client.send_post(content)

    def follow_user(self, did: str):
        self.client.follow(did)

    def unfollow_user(self, did: str):
        self.client.unfollow(did)

    def get_did_from_handle(self, handle: str) -> str:
        return self.client.resolve_handle(handle)

    def search_users_by_keyword(self, keyword: str, limit: int = 10) -> list[dict]:
        results = self.client.app.bsky.actor.search_actors({'term': keyword, 'limit': limit})
        actors = results.actors if results and results.actors else []

        return [
            {
                "handle": actor.handle,
                "display_name": actor.display_name,
                "description": actor.description,
                "did": actor.did
            }
            for actor in actors
        ]

    def get_profile(self, did: str) -> dict:
        return self.client.get_profile(did).__dict__

# if __name__ == "__main__":
#    load_dotenv()
#    handle = os.getenv("BSKY_HANDLE")
#    password = os.getenv("BSKY_APP_PASSWORD")

#    bot = BlueskyBot(handle, password)
#    bot.post_message("This is a test post.")