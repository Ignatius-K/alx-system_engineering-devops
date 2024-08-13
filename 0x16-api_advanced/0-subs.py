#!/usr/bin/python3
"""API advanced development"""

from requests import Request, Session


def number_of_subscribers(subreddit):
    """Get the number of subscribers

    Queries the Redit endpoint to get subscribers
    of particular subreddit

    Return:
        (int): The number of subscribers, 0 if invalid subreddit
    """
    request = Request(
        method='GET',
        url='https://www.reddit.com/subreddits/search.json',
        params={
            'q': subreddit
        },
    )

    session = Session()
    preparedrequest = session.prepare_request(request)
    subscribers = 0

    try:
        response = session.send(preparedrequest, allow_redirects=False)
        response.raise_for_status()
        response = response.json()
        data = response.get('data').get('children')[0].get('data')
        subscribers = data.get('subscribers')
    except Exception as e:
        pass
    return subscribers
