import asyncio
import logging

from requests_html import AsyncHTMLSession, HTMLSession

urls_store = []


def pre_download(url):
    """
    Decorator to get all urls that should be pre-downloaded
    """

    def wrapper(func):
        urls_store.append(url)
        return func

    return wrapper


async def get_link(url, asession):
    """
    Async get link
    """
    r = await asession.get(url)

    logging.info("Finished getting url %s", url)
    return (url, r)


def update_cache(cache):
    """
    Updates the Cache
    """
    asyncio.set_event_loop(asyncio.new_event_loop())

    asession = AsyncHTMLSession()
    tasks = []

    for url in urls_store:
        tasks.append(lambda url=url: get_link(url, asession))

    results = asession.run(*tasks)

    for url, result in results:
        cache[url] = result


def update_one(cache, url):
    """
    Updates the for one URL
    """

    asyncio.set_event_loop(asyncio.new_event_loop())

    session = HTMLSession()

    result = session.get(url)

    cache[url] = result
