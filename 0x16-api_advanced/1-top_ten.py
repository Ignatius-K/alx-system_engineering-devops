#!/usr/bin/python3

"""Advanced Reddit API querying"""


from requests import Request, Session


def top_ten(subreddit):
    """Get top ten posts

    Get the top ten posts in a subreddit

    Args:
        subreddit (str): The title of the subreddit

    Return:
        (list|None): Title of top ten posts otherwise None
    """

    if not subreddit:
        return None

    default_limit = 10

    request = Request(
        method='GET',
        url=f'https://oauth.reddit.com/r/{subreddit}/top.json',
        params={
            'limit': default_limit
        }
    )

    session = Session()
    session.headers.update({
        'User-Agent': 'Windows 10:myRedditApp:version1.0 (by /u/natius-k)'
    })
    prepared_request = session.prepare_request(request)

    try:
        response = session.send(prepared_request, allow_redirects=False)
        response.raise_for_status()
        data = response.json().get('data')
        if (data.get('dist') and data.get('dist') > 0):
            posts = data.get('children')
            for post in posts:
                print(post.get('data').get('title'))
    except Exception as e:
        print(None)
