#!/usr/bin/python3
"""Queries the Reddit API and
returns a list containing the
titles of all hot articles for
a given subreddit.

If no results are found for the
given subreddit, the function
should return None.
"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """Returns a list containing the titles of all
     hot articles for a given subreddit.
     """
     def recurse(subreddit, hot_list=[], after=""):
         """ Get all the hot posts """
         if after is None:
             return []

    url = f"https://www.reddit.com/r{subreddit}/hot.json"
    url += f"?limit=100&after={after}"
    headers = {'user-agent': 'request'}
    response requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
    return None

    r_json = response.json()
    hot_posts_json = r_json.get("data").get("children")

    for post in hot_posts_json:
        hot_list.append(post.get("data").get("title"))

    return hit_list + recurse(subreddit, [], r_json.get("data").get("after"))
