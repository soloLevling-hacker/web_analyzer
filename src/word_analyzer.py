from collections import Counter
from string import punctuation
import re

def extract_words(soup):
    if not soup:
        return []

    # Remove unwanted tags
    for bad in soup(["script", "style", "noscript"]):
        bad.decompose()

    text = soup.get_text(separator=" ").lower()
    text = re.sub(r'\s+', ' ', text)

    # Remove punctuation
    text = "".join(ch for ch in text if ch not in punctuation)

    words = text.split()
    return words


def count_words(words, limit=20):
    freq = Counter(words)
    return freq.most_common(limit)
