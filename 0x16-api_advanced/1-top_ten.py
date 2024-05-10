#!/usr/bin/python3
"""Queries the Reddit API and
prints the titles of the first
10 hot posts listed for a given
subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first10 hot posts listed for a given subreddit.
    """
    # Set the Default URL strings
    base_url = 'https://www.reddit.com'
    api_uri = '{base}/r/{subreddit}/hot.json'.format(base=base_url,
                                                        subreddit=subreddit)

    # Set an User-Agent
    user_agent = {'User-Agent': 'MyRedditBot/1.0'}

    # Set the Query Strings to Request
    params = {'limit': '10'}

    # Get the Response of the Reddit API
    res = requests.get(api_uri, headers=user_agent,
                        params=params, allow_redirects=False)

    # Checks if the subreddit is invalid
    if res.status_code != 200:
        print('None')
        return

    #parse JSON response
    data= res.json()

    # check for errors in the JSON response
    if 'error' in data:
        print('None')
        return

    # Extract post titles and print them
    posts = data.get('data', {}).get('children', [])
    for post in posts:
        post_data = post.get('data', {})
        title = post_data.get('title')
        if title:
            print(title)
