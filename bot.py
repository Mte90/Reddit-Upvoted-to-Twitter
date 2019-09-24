#! /usr/bin/python3
import praw
import os

reddit = praw.Reddit('mte90')

print("Logged in as: " + str(reddit.user.me()))
print()

user = reddit.redditor('mte90')
posts = {}

if os.path.exists('./posts.json'):
    f = open("./posts.json", "r")
    posts = f.read()

for post in user.upvoted(limit=100):
    print(post.id)
    posts[post.id].append({'title': post.title, 'subreddit': str(post.subreddit).lower()})
#    print(post.title + ' - ' + str(post.subreddit) + ' - ' + post.id + ' - ' + post.permalink)

print(posts)