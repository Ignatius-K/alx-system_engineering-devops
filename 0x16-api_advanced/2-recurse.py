#!/usr/bin/python3

"""Advanced Reddit API testing"""

import requests

# session = Session()
# session.headers.update({
#     'User-agent': 'Linux/5.4.0 MyRedditApp/2.3 (by /u/natius-k)'
# })


def recurse(subreddit, hot_list=[], after=""):
    """Gets hot topics"""
    response = requests.get(
        f'https://www.reddit.com/r/{subreddit}/hot.json',
        headers={"User-Agent": "Mozilla 5.0"},
        params={"after": after},
    )
    if response.status_code == 200:
        for _data in response.json().get('data').get('children'):
            data = _data.get('data')
            hot_list.append(data.get('title'))
        after = response.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None

# def recurse(subreddit, hot_list=[], after=None):
#     """recurse - Query API recursively

#     Args:
#         subreddit (str): the subreddit title
#         count (int): the count of posts
#         after (str|None): the token of next request

#     Return:
#         (int): the count of posts
#     """
#     request = Request(
#         method='GET',
#         url=f'https://oauth.reddit.com/r/{subreddit}/hot.json',
#     )
#     if (after is not None):
#         request.params = {'after': after}

#     prepared_request = session.prepare_request(request)
#     try:
#         response = session.send(prepared_request)
#         response.raise_for_status()
#         response = response.json()
#         data = response.get('data')
#         after = data.get('after')
#         dist = data.get('dist')
#         if (dist is not None and type(dist) is int):
#             hot_list.extend(data.get('children'))
#         if (after is None):
#             return hot_list
#         return recurse(subreddit, hot_list=hot_list, after=after)
#     except exceptions.HTTPError as e:
#         return hot_list
