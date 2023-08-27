#! /usr/bin/python3
import os
import json
import praw
import time
import tweepy
import configparser

# Load custom settings from PRAW official file
if os.path.exists('./praw.ini'):
    praw_config = configparser.RawConfigParser()
    praw_config.read_file(open('./praw.ini'))

def save_tweets(posts):
    with open('posts.json', 'w') as outfile:
        print("\nPost saved")
        json.dump(posts, outfile, indent=4)

reddit = praw.Reddit(str(praw_config.get('user', 'nickname')))

print("Logged in as: " + str(reddit.user.me()))
print()

user = reddit.redditor(str(praw_config.get('user', 'nickname')))
posts = {}

# Load settings for tweepy
if os.path.exists('./tweepy.ini'):
    tweepy_config = configparser.RawConfigParser()
    tweepy_config.read_file(open('./tweepy.ini'))
else:
    print('tweepy.ini missing')

# Authenticate to Twitter
api = tweepy.Client(consumer_key=str(tweepy_config.get('tweepy', 'consumer_key')),consumer_secret=str(tweepy_config.get('tweepy', 'consumer_secret')),access_token=str(tweepy_config.get('tweepy', 'access_token')),access_token_secret=str(tweepy_config.get('tweepy', 'access_secret')))

if os.path.exists('./posts.json'):
    print("File posts found")
    with open('./posts.json') as json_file:
        posts = json.load(json_file)
        print("Posts item: " + str(len(posts)))

excludes = str(praw_config.get('user', 'exclude'))
excludes = excludes.split(',')

for post in user.upvoted(limit=100):
    if post.id not in posts:
        tweet_it = True
        print("Missing " + post.id + " post")

        for exclude in excludes:
            if exclude.lower() == str(post.subreddit).lower():
                tweet_it = False
                break

        if 'crosspost_parent_list' in vars(post):
            if str(post.author.name).lower() == praw_config.get('user', 'nickname'):
                print("Crosspost of the user that is also the author, avoid publishing - ignored")
                continue

        if 'u_' + str(praw_config.get('user', 'nickname')) == str(post.subreddit).lower():
            continue

        if tweet_it:
            posts[post.id] = {'title': post.title, 'subreddit': str(post.subreddit).lower(), 'permalink': post.permalink}
            # Create a tweet
            print('Posting new tweet')
            save_tweets(posts)
            try:
                api.create_tweet(text=post.title + ' via /r/' + str(post.subreddit) + "\nhttps://www.reddit.com" + post.permalink)
            except:
                print('Error from Twitter API')
            # Wait 10 minutes before tweet it
            time.sleep(600)
