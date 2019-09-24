#! /usr/bin/python3
import praw

reddit = praw.Reddit('mte90')

print(reddit.user.me())

print("Logged in as: " + str(reddit.user.me()))
print()

user = reddit.redditor('mte90')

for post in user.upvoted(limit=100):
    print(post.title + ' - ' + str(post.subreddit) + ' - ' + post.id + ' - ' + post.permalink)
