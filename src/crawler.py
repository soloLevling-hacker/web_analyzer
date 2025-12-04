from urllib.parse import urlparse
from .utils import get_soup
from .link_checker import extract_links

def crawl_internal(url, limit=5):
    soup = get_soup(url)
    if not soup:
        return []

    base_domain = urlparse(url).netloc
    links = extract_links(url, soup)

    internal = []

    for link in links:
        if len(internal) >= limit:
            break

        if base_domain in link:
            internal.append(link)

    return internal
