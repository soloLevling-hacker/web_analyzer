def extract_meta(soup):
    if not soup:
        return {}

    data = {}

    # Title
    title_tag = soup.find("title")
    data["title"] = title_tag.text.strip() if title_tag else "N/A"

    # Description
    desc = soup.find("meta", attrs={"name": "description"})
    data["description"] = desc.get("content") if desc else "N/A"

    # Keywords
    keys = soup.find("meta", attrs={"name": "keywords"})
    data["keywords"] = keys.get("content") if keys else "N/A"

    # Language
    html_tag = soup.find("html")
    data["language"] = html_tag.get("lang") if html_tag and html_tag.has_attr("lang") else "unknown"

    return data
