import os
import yaml
import json
import praw
import requests


class RedditData:
    def __init__(self):
        self.client_id= os.environ['REDDIT_CLIENT_ID']
        self.client_secret= os.environ['REDDIT_CLIENT_SECRET']
        self.username = os.environ['REDDIT_USERNAME']
        self.password = os.environ['REDDIT_PASSWORD']
        self.user_agent = os.environ['REDDIT_USER_AGENT']
                
    def auth(self):
        reddit = praw.Reddit(client_id=self.client_id,
                             client_secret= self.client_secret,
                             username= self.username,
                             password= self.password,
                             user_agent= self.user_agent)
        reddit.read_only = True    
        return reddit
    
    def get_posts(self, sub, limit_posts, filterby):
        reddit = self.auth()
        subreddit = reddit.subreddit(sub)
        if filterby.lower() == 'top':
            posts = subreddit.top(limit=int(limit_posts))
        elif filterby.lower() == 'hot':
            posts = subreddit.hot(limit=int(limit_posts))
        elif filterby.lower() == 'new':
            posts = subreddit.new(limit=int(limit_posts))
        else:
            posts = subreddit.hot(limit=int(limit_posts))
        return posts

