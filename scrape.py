import os
import requests
from bs4 import BeautifulSoup as bs
import urllib.parse
from time import sleep

base_url = "https://www.classcentral.com"
desired_url = ''
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'}


if not os.path.exists("output"): # One level deep scraping > html pages output
    os.makedirs("output")

response = requests.get(base_url, headers=headers)
soup = bs(response.content, 'html.parser')

images = soup.find_all('img', {'data-src' : True}) # Change all the img tag src
for image in images:
    image['src'] = image['data-src']
    del image['data-src']

fav_icon = soup.find_all('link') # To fix the favicon in link tags
for link_tag in fav_icon:
    if link_tag.has_attr('href'):
        href = link_tag['href']
        href_url = urllib.parse.urljoin(base_url,href)
        link_tag['href'] = href_url

links =  soup.find_all('a')
l = [] # Fixed from slug hyperlinklist 
for link in links: # To get hyperlinks one level deep
    href = link.get('href').strip()
    if href.startswith('https')or href.startswith('http'):
        l.append(href)
    else:
        l.append(base_url+href)
        
yt = 'https://www.youtube.com/classcentral'
tw = 'https://www.twitter.com/classcentral'
li = 'https://www.linkedin.com/company/classcentral'
fb = 'https://www.facebook.com/classcentral'
fb1 = 'http://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.classcentral.com%2F'
tw1 = 'https://twitter.com/intent/tweet?url=https%3A%2F%2Fwww.classcentral.com%2F&text=&via=classcentral'
l = [i for i in l if i not in [yt,tw,li,fb,fb1,tw1]]

for i in l: # Editing filenames from hyperlinks
    file_name = i.replace(base_url ,"").replace("/","_")+'.html'
    if file_name in os.listdir('output/'):
        continue
    with open('output/'+file_name, 'w') as f:
        response = requests.get(i, headers=headers)
        sleep(5)
        soup1 = bs(response.content, 'html.parser')
            
        images = soup1.find_all('img', {'data-src':True})#Fix img src - data-src links
        for image in images:
            if image['data-src']:
                image['src'] = image['data-src']
                
        a_tags = soup1.find_all('a') # To delete a_tags and hyperlinks to make it 1.level deep scraping
        links_href = [i['href'] for i in links]
        for a_tag in a_tags: # Deleting Process
            if a_tag['href'] not in links_href and a_tag['href'] != '/' and a_tag['href'] != base_url:
                    del a_tag['href']
                
            if a_tag.has_attr('href'):
                href = a_tag['href']
                if href.startswith(base_url):
                    href_url = href.replace(base_url, desired_url)
                    a_tag['href'] = href_url
                
            
        fvicons = soup1.find_all('link') # To fix favicons href
        for fvicon in fvicons:
            if fvicon.has_attr('href'):
                href_fvicon = fvicon['href']
                href_url_fvicon = urllib.parse.urljoin(base_url, href_fvicon)
                fvicon['href'] = href_url_fvicon
        f.write(str(soup1))
        
a_tags = soup.find_all('a') # To blind all the a tag href links from org site homepage
for a_tag in a_tags:
    if a_tag.has_attr('href'):
        href = a_tag['href']
        if href.startswith(base_url):
            href_url = href.replace(base_url, desired_url)
            a_tag['href'] = href_url
        
with open('index.html', 'w') as f:# To save index html on base_dir
    f.write(str(soup))
