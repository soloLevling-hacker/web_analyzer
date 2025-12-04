import requests
from urllib.parse import urljoin, urlparse

def extract_links(url, soup):
    if not soup:
        return []

    anchors = soup.find_all("a")
    links = set()

    for a in anchors:
        href = a.get("href")
        if href and not href.startswith("#"):
            full = urljoin(url, href)
            links.add(full)

    return list(links)


def check_link(url):
    try:
        r = requests.head(url, timeout=5)
        return r.status_code < 400
    except:
        return False
