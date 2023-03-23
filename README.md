<div align="center">

# ***Web Scraper for CodingAllStars***
</div>
<hr>

### ***No HTTrack, No Other Third Party Apps...Only Pure Python Scripts. One Level Deep Scraping of classcentral.com***

- ##### BeautifulSoup 4
- ##### requests
- ##### os
- ##### urllib
- ##### deep_translator
- ##### re
- ##### json

This code is a web scraper that scrapes a website called "classcentral.com". The scraper saves the HTML content of the website's pages into separate files in a directory called "output". The scraper also manipulates some of the links, images, and favicon sources to make them valid URLs.

The code starts by importing some necessary modules and defining some variables such as the base URL, desired URL, and user agent header. It then checks if the "output" directory exists and creates it if it doesn't.

The code then sends a GET request to the base URL using the requests module and extracts the HTML content using the BeautifulSoup module. It finds all the img tags with data-src attributes and replaces the src attributes with the data-src attributes. It also fixes the favicon links by joining the base URL with the href attributes.

Next, the code finds all the anchor tags and appends their href attributes to a list. It removes any duplicate URLs and any links to the website's social media pages. It also ensures that the URLs are valid by joining them with the base URL if they are relative.

The code then iterates over the list of URLs and saves the HTML content of each URL to a file in the "output" directory. It fixes any broken image links by replacing the src attributes with the data-src attributes. It also removes any anchor tags that link to pages that are not within the one-level-deep scraping limit. Finally, it fixes the favicon links by joining them with the base URL.

The code also manipulates the anchor tags on the base URL's HTML content to blind their href attributes to the original website's URLs. It then saves the HTML content of the base URL to a file named "index.html".

Overall, this code scrapes the "classcentral.com" website while fixing broken image and favicon links, ensuring the validity of the URLs, and performing one-level-deep scraping. It also adds a delay between requests to avoid getting blocked by CDNs.

Used regular expression module and deep_tranlator library to translate the text between tags to Hindi language with the code inside of translate.py.To not make often Api calls to google, i used a cache_dict:dictionary variable to store the translated words and at the end of the translation i dumped the cached data from the variable to dict.json file and saved locally in projects folder, later on the process i used this file to translate the words of other html pages which stored in this file. This method speeded up the translation process and if word doesnt get any match in dict, process contiuned to make api calls to google to translate the words and store them as cached data.