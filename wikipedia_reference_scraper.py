import requests
from bs4 import BeautifulSoup


def get_url_page(url):
    page = requests.get(url)
    if page.status_code == 200:
        return page.text
    else:
        print('Check the url entered')


def get_references(url):
    page_text = get_url_page(url)
    soup = BeautifulSoup(page_text, 'html.parser')
    citations = soup.find_all('cite')
    return citations


def write_to_document(url, document_name):
    with open(document_name, 'w') as file:
        for citation in get_url_page(url):
            file.write('\n\n')
            for string in citation.strings:
                file.write(string)










