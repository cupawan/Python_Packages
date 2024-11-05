import os
import tweepy

class TwitterCreateTweet:
    def __init__(self):
        self.client, self.c = self.authenticate_twitter()

    def authenticate_twitter(self):
        client = tweepy.Client(
            consumer_key=os.environ["TWITTER_CONSUMER_KEY"],
            consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"],
            access_token=os.environ["TWITTER_ACCESS_TOKEN"],
            access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"])
        auth = tweepy.OAuth1UserHandler(os.environ["TWITTER_CONSUMER_KEY"], os.environ["TWITTER_CONSUMER_SECRET"])
        auth.set_access_token(os.environ["TWITTER_ACCESS_TOKEN"], os.environ["TWITTER_ACCESS_TOKEN_SECRET"])
        c = tweepy.API(auth)
        return client, c
    
    def post_tweet(self,text,media_paths = None):
        media_ids = [self.c.media_upload(media_path).media_id for media_path in media_paths] if media_paths else None
        response = self.client.create_tweet(text = text, media_ids = media_ids)
        if len(response.errors) == 0:
            print("Tweet Posted Successfully")
            return response
        else:
            print("Not Posted, Errors: ", response.errors)
            return None