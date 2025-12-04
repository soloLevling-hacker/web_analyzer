import requests
from bs4 import BeautifulSoup

def get_soup(url):
    try:
        r = requests.get(url, timeout=10, headers={"User-Agent": "Mozilla/5.0"})
        r.raise_for_status()
        return BeautifulSoup(r.text, "lxml")
    except Exception as e:
        print(f"[!] Failed to fetch {url} -> {e}")
        return None


def clean_text(text):
    return text.replace("\n", " ").replace("\r", " ").strip()
