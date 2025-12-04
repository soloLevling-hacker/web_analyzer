# Web Analyzer

**Web Analyzer** is a Python project that explores websites by extracting meta tags, headings, images, and word frequencies. Users can save results in TXT, JSON, or CSV. It’s designed for students and beginners to practice web scraping, learn Python, and understand website structures while having fun coding.

---

## Features

- Extract website **meta tags** (title, description, keywords)  
- Get all **headings** (`h1`-`h6`)  
- Analyze **word frequency** and ignore common stopwords  
- Extract **images and alt text**  
- Save results in **TXT, JSON, or CSV** formats  

---

## Installation

1. Clone the repository:  
```
git clone https://github.com/yourusername/web_analyzer.git
cd web_analyzer
Install dependencies:

Copy code
pip install -r requirements.txt
Usage
Run the main program:

Copy code
python app.py
Enter the website URL when prompted.

The program will display meta tags, headings, paragraphs, and images.

Choose a file format to save the results.

Project Structure
Copy code
web_analyzer/
│
├── app.py
├── requirements.txt
│
└── src/
    ├── meta_scraper.py
    ├── word_analyzer.py
    ├── image_extractor.py
    ├── link_checker.py
    ├── crawler.py
    └── utils.py
Contributing
Feel free to fork, add new features, or improve code! This project is perfect for students who want to learn web scraping and Python in a fun, hands-on way.
