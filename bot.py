#! /usr/bin/python3
import praw
import os
import json

reddit = praw.Reddit('mte90')

print("Logged in as: " + str(reddit.user.me()))
print()

user = reddit.redditor('mte90')
posts = {}

if os.path.exists('./posts.json'):
    print("File JSON found")
    with open('./posts.json') as json_file:
        posts = json.load(json_file)

for post in user.upvoted(limit=100):
    if post.id not in posts:
        posts[post.id] = {'title': post.title, 'subreddit': str(post.subreddit).lower(), 'permalink': post.permalink}
        print("Missing " + post.id + " post")

with open('posts.json', 'w') as outfile:
    print("JSON saved")
    json.dump(posts, outfile, indent=4)
