from requests_html import AsyncHTMLSession

all_urls = []

def pre_download(url):
    """
    Decorator to get all urls that should be pre-downloaded
    """
    def pseudo_decorator():
        def real_wrapper(function_arguments):
            print(function_arguments)
            all_urls.append(url)

        return real_wrapper
    return pseudo_decorator

async def get_link(url, asession):
    """
    Async get link
    """
    r = await asession.get(url)
    return r


def update_cache(cache):
    """
    Updates the Cache
    """

    asession = AsyncHTMLSession()
    tasks = []

    for url in all_urls:
        tasks.append(get_link(url, asession))

    results = asession.run(tasks)

    for url, result in zip(url, results):
        cache[url] = result
