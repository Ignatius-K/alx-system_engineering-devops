#!/usr/bin/python3
"""API advanced development"""

import requests


def number_of_subscribers(subreddit):
    """Gets subscribers on given reddit
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        results = response.json().get("data")
        return results.get("subscribers")
    return 0

# def number_of_subscribers(subreddit):
#     """Get the number of subscribers

#     Queries the Redit endpoint to get subscribers
#     of particular subreddit

#     Return:
#         (int): The number of subscribers, 0 if invalid subreddit
#     """
#     request = Request(
#         method='GET',
#         url='https://www.reddit.com/subreddits/search.json',
#         params={
#             'q': subreddit
#         },
#     )

#     session = Session()
#     session.headers.update({
#         'User-agent': 'Linux/5.4.0 MyRedditApp/2.3 (by /u/natius-k)'
#     })
#     preparedrequest = session.prepare_request(request)
#     subscribers = 0

#     try:
#         response = session.send(preparedrequest, allow_redirects=False)
#         response.raise_for_status()
#         response = response.json()
#         data = response.get('data').get('children')[0].get('data')
#         subscribers = data.get('subscribers')
#     except Exception as e:
#         pass
#     return subscribers
