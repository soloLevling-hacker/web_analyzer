from src.utils import get_soup
from src.meta_scraper import extract_meta
from src.word_analyzer import extract_words, count_words
from src.image_extractor import extract_images
from src.link_checker import extract_links, check_link
from src.crawler import crawl_internal

def main():
    url = input("Enter URL: ").strip()
    print("\n[+] Fetching page...")
    soup = get_soup(url)

    print("\n=== META DATA ===")
    meta = extract_meta(soup)
    for k, v in meta.items():
        print(f"{k}: {v}")

    print("\n=== WORD ANALYSIS ===")
    words = extract_words(soup)
    freq = count_words(words)
    print(f"Total words: {len(words)}")
    for w, f in freq:
        print(f"{w} -> {f}")

    print("\n=== IMAGES FOUND ===")
    imgs = extract_images(url, soup)
    for img in imgs:
        print(f"{img['url']} (alt='{img['alt']}')")

    print("\n=== LINKS ===")
    links = extract_links(url, soup)
    for link in links:
        status = "OK" if check_link(link) else "BROKEN"
        print(f"{link} ---> {status}")

    print("\n=== INTERNAL CRAWL (1-LEVEL) ===")
    internal = crawl_internal(url)
    for i in internal:
        print(i)


if __name__ == "__main__":
    main()
