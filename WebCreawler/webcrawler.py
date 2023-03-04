import requests
import json
from bs4 import BeautifulSoup
import io

import requests
import warcio


index_list = ["2020-50","2020-45","2020-40","2020-34","2020-29","2020-24","2020-16", "2020-10", "2020-05"]
# index_list = ["2020-50"]


def search_domain(domain):

    record_list = []
    
    print("[*] Trying target domain: %s" % domain)
    
    for index in index_list:
        
        print("[*] Trying index %s" % index)
        
        cc_url  = "http://index.commoncrawl.org/CC-MAIN-%s-index?" % index
        cc_url += "url=%s&matchType=domain&output=json" % domain
        
        response = requests.get(cc_url)
        
        if response.status_code == 200:
            
            records = response.content.splitlines()
            
            for record in records:
                record_list.append(json.loads(record))
            
            print("[*] Added %d results." % len(records))
            
    
    print("[*] Found a total of %d hits." % len(record_list))
    
    return record_list        

def extract_external_links(html_content, output, url):

    parser = BeautifulSoup(html_content, 'html.parser')
        # parser.b
    links1 = parser.find_all("covid")
    links2 = parser.find_all("economy")
    if links1:
        for link in links1:
            output.append(link)
            output.append(url)

domains = ['cnn.com', 'bloomberg.com', 'economist.com', 'worldbank.org', 'usa.gov/coronavirus']
# domains = ['economist.com']
output = []
for domain in domains:
    record_list = search_domain(domain)
    print(record_list)

    for record in record_list:
        warc_filename = record['filename']
        warc_record_offset = int(record['offset'])
        warc_record_length = int(record['length'])
        url = record['url']
        response = requests.get(f'https://data.commoncrawl.org/{warc_filename}',
                            headers={'Range': f'bytes={warc_record_offset}-{warc_record_offset + warc_record_length - 1}'})
        with io.BytesIO(response.content) as stream:
            for htmlRecord in warcio.ArchiveIterator(stream):
                html = htmlRecord.content_stream().read()
                extract_external_links(html, output, url)
print(output)
            