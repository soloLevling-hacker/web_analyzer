from urllib.parse import urljoin

def extract_images(url, soup):
    if not soup:
        return []

    imgs = soup.find_all("img")
    results = []

    for img in imgs:
        src = img.get("src")
        alt = img.get("alt", "")
        if src:
            full = urljoin(url, src)
            results.append({"url": full, "alt": alt})

    return results
