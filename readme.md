# Reddit Post Upvoted by you to Twitter 

The idea is to share on Twitter the upvoted post but excluding posts from specific subreddits.

## Requirements

`pip3 install -r requirements.txt`

## Install

Copy `praw-sample.ini` and `tweeepy-sample.ini` and put your settings.  
Require a Twitter and Reddit app with their token in the config files.

## How works

This script generate a `posts.json` at every run with the list of posts to check if already posted.