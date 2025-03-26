import argparse
import os
from collections import deque
from urllib.parse import urljoin, urlparse, unquote
import requests
from bs4 import BeautifulSoup

def extract_text(html):
    soup = BeautifulSoup(html, 'html.parser')

    for tag in soup(['script', 'style', 'nav', 'footer', 'head', 'header', 'aside']):
        tag.decompose()

    for element in soup.find_all(['li', 'dd', 'dt', 'div', 'p', 'br']):
        element.append(' ')

    text = soup.get_text()
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    return '\n'.join(chunk for chunk in chunks if chunk)

def extract_links(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    links = []

    for a in soup.find_all('a', href=True):
        absolute_url = urljoin(base_url, a['href'])
        parsed = urlparse(absolute_url)
        parsed = parsed._replace(fragment='', query='')
        normalized_url = parsed.geturl()
        
        if normalized_url not in links:
            links.append(normalized_url)

    return links

def crawl_pages(urls, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    visited = set()
    queue = deque(urls)
    doc_counter = 0
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; AcademicCrawler/1.0)'}

    with open('index.txt', 'w', encoding='utf-8') as index_file:
        while queue and doc_counter < 100:
            url = queue.popleft()

            if url in visited:
                continue
            visited.add(url)

            try:
                response = requests.get(url, headers=headers, timeout=10)
                if 'text/html' not in response.headers.get('Content-Type', ''):
                    continue
                response.raise_for_status()
            except Exception as e:
                print(f"Error fetching {url}: {e}")
                continue

            text_content = extract_text(response.text)
            word_count = len(text_content.split())

            if word_count < 1000:
                continue

            doc_counter += 1
            filename = os.path.join(output_dir, f'doc{doc_counter}.txt')
            with open(filename, 'w', encoding='utf-8') as doc_file:
                doc_file.write(text_content)

            decoded_url = unquote(url)
            index_file.write(f'{doc_counter}\t{decoded_url}\n')
            index_file.flush()
            print(f'Saved: {filename} ({word_count} words)')
                
            new_links = extract_links(response.text, url)
            for link in new_links:
                if link not in visited and link not in queue:
                    queue.append(link)

    print(f'Crawling complete. Downloaded {doc_counter} documents to "{output_dir}" directory.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Web crawler')
    parser.add_argument('urls', nargs='+', help='Initial URLs to start crawling from')
    args = parser.parse_args()

    crawl_pages(args.urls, 'docs')
