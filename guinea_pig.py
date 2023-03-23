# from bs4 import BeautifulSoup

# # Open the HTML file and read its contents
# with open('index.html') as file:
#     html = file.read()

# # Parse the HTML using BeautifulSoup
# soup = BeautifulSoup(html, 'html.parser')

# # Select all the images with data-src attribute
# images = soup.find_all('img', {'data-src': True})

# # Loop through each image and update the src attribute with the value of data-src
# for image in images:
#     image['src'] = image['data-src']
#     # Remove the data-src attribute from the image
#     del image['data-src']

# # Save the updated HTML to a new file
# with open('updated_html_file.html', 'w') as file:
#     file.write(str(soup))
# ############# img data-src changer############################################








# from bs4 import BeautifulSoup as soup
# from urllib.request import urlopen
# from urllib.request import Request, urlopen


# url = "https://www.classcentral.com/"
# req = Request(url , headers={'user-agent': 'My-App/0.0.1'})
# # page = urlopen(url)
# webpage = urlopen(req).read().decode("utf-8")
# page_soup = soup(webpage, "html.parser")

# # html = page.read().decode("utf-8")
# # soup = BeautifulSoup(html, "html.parser")
# links_containers = page_soup.findAll("a")
# dict1 = {'link text': [], 'link url': []}
# for i in links_containers:
#     link = i['href']
#     text = i.text.strip()

# #     if link[0]=='/':
# #         link = "https://www.classcentral.com"+link

# #     if text =='RSS Feed':
# #         pass
# #     req = Request(link , headers={'User-Agent': 'Mozilla/5.0'})
# #     webpage_links = urlopen(req).read().decode("utf-8")
# #     page_soup_links = soup(webpage_links, "html.parser")
# #     tag_links = page_soup_links.body
# #     link_content=[]
# #     for j in tag_links.strings:
# #         s=j.strip()
# #         if s=="":
# #             pass
# #         else:
# #             link_content.append(s)
#     if link == '/':
#         continue
#     if not 'link text' and not 'link url' in dict1:
#         dict1['link text']=[text]
#         dict1['link url']=[link]
#     else:
#         dict1['link text'].append(text)
#         dict1['link url'].append(link)
    
# print(dict1)
# print(len(dict1['link url']))
##################link finder len calculator##################################







# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait

# options = webdriver.ChromeOptions()
# options.add_argument("--headless") # run Chrome in headless mode
# options.add_argument("--disable-dev-shm-usage") # disable shared memory
# options.add_argument("--no-sandbox") # disable sandbox mode
# driver = webdriver.Chrome(options=options)


# url = "https://classcentral.com/"
# driver.get(url)

# html_content = driver.page_source

# with open("index.html", "w") as f:
#     f.write(html_content)

# driver.quit()
######################  html parser_saver #####################################






# from selenium import webdriver
# import os
# import requests

# # create a directory to store the CSS and JS files
# if not os.path.exists("css"):
#     os.makedirs("css")
# if not os.path.exists("js"):
#     os.makedirs("js")

# # set up the Selenium driver
# options = webdriver.ChromeOptions()
# options.add_argument("--headless") # run Chrome in headless mode
# options.add_argument("--disable-dev-shm-usage") # disable shared memory
# options.add_argument("--no-sandbox") # disable sandbox mode
# driver = webdriver.Chrome(options=options)

# # navigate to the website
# url = "https://classcentral.com/"
# driver.get(url)

# # get the HTML content and save it to a file
# html_content = driver.page_source
# with open("index.html", "w") as f:
#     f.write(html_content)

# # find all links to CSS files and download them
# for link in driver.find_elements_by_tag_name("link"):
#     rel = link.get_attribute("rel")
#     if rel and "stylesheet" in rel:
#         css_url = link.get_attribute("href")
#         if css_url:
#             css_file = os.path.join("css", os.path.basename(css_url))
#             with open(css_file, "wb") as f:
#                 f.write(requests.get(css_url).content)

# # find all script tags and download the JavaScript files
# for script in driver.find_elements_by_tag_name("script"):
#     src = script.get_attribute("src")
#     if src:
#         js_file = os.path.join("js", os.path.basename(src))
#         with open(js_file, "wb") as f:
#             f.write(requests.get(src).content)

# # close the browser
# driver.quit()


# # Close the browser
# driver.quit()
###############################################################################

# import os
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin


# url = "https://classcentral.com/"


# if not os.path.exists("css"):
#     os.makedirs("css")
# if not os.path.exists("js"):
#     os.makedirs("js")

# agent = {'user-agent' : 'my-app/0.0.1'}
# response = requests.get(url)


# soup = BeautifulSoup(response.content, "html.parser")

# for link in soup.find_all("link", {"rel": "stylesheet"}):
#     css_url = link.get("href")
#     if css_url:
#         css_url = urljoin(url, css_url)
#         css_file = os.path.join("css", os.path.basename(css_url))
#         with open(css_file, "wb") as f:
#             f.write(requests.get(css_url).content)
#         # replace the original URL with the local file path
#         link["href"] = css_file


# for script in soup.find_all("script", {"src": True}):
#     js_url = script["src"]
#     if js_url.startswith("//"):
#         js_url = "https:" + js_url
#     js_url = urljoin(url, js_url)
#     js_file = os.path.join("js", os.path.basename(js_url))
#     with open(js_file, "wb") as f:
#         f.write(requests.get(js_url).content)
#     # replace the original URL with the local file path
#     script["src"] = js_file


# with open("index.html", "w") as f:
#     f.write(str(soup))
##############################################################################
# import requests
# import os
# from bs4 import BeautifulSoup
# from urllib.parse import urlparse, urlunparse


# url = "https://www.classcentral.com/"
# agent = {'user-agent': 'my-app/0.0.1'}
# response = requests.get(url,headers=agent)

# html_content = response.content
# soup = BeautifulSoup(html_content,'lxml')

# with open('index.html','wb') as f:
#     f.write(html_content)

# url = 'https://www.classcentral.com/'
# response = requests.get(url)

# soup = BeautifulSoup(response.text, 'lxml')
# css_links = [link['href'] for link in soup.find_all('link', rel='stylesheet')]
# js_links = [script['src'] for script in soup.find_all('script', src=True)]

# for link in css_links + js_links:
#     parsed_link = urlparse(link)
#     if not parsed_link.scheme:
#         parsed_link = parsed_link._replace(scheme='https')
#     if not parsed_link.netloc:
#         parsed_link = parsed_link._replace(netloc=urlparse(url).netloc)
#     fixed_link = urlunparse(parsed_link)
#     filename = os.path.basename(fixed_link)
#     filepath = os.path.join('/home/alice/Coding_Allstars_Interview/',filename)
    
#     with open(filepath,'wb') as f:
#         f.write(requests.get(fixed_link).content)

# html_content = str(soup)
# css_content = [open(os.path.join('/home/alice/Coding_Allstars_Interview/', \
#                 os.path.basename(link))).read() for link in css_links]
# js_content = [open(os.path.join('/home/alice/Coding_Allstars_Interview/', \
#                 os.path.basename(link))).read() for link in js_links]
