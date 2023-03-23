# from googletrans import Translator
# from bs4 import BeautifulSoup as bs

# with open('index_en.html', 'r', encoding='utf-8') as f:
#     html = f.read() 
# soup = bs(html, 'html.parser')

# text_elements = [element for element in soup.find_all(string=True) if element.parent.name not in ['script', 'style']]


# translator = Translator()
# for element in text_elements:
#     text = element.strip()
#     if not text:
#         continue
#     translated_text = translator.translate(text, dest='hi').text
#     element.replace_with(translated_text)

# with open('index.html', 'w', encoding='utf-8') as f:
#     f.write(soup.prettify())






# from deep_translator import GoogleTranslator
# import os

# input_folder = 'output'
# output_folder = 'output_hindi'

# # Create the output folder if it does not exist
# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# # Set the maximum length of the input text
# max_len = 5000

# # Iterate over all HTML files in the input folder
# for filename in os.listdir(input_folder):
#     if filename.endswith('.html'):
#         # Read the HTML file
#         with open(os.path.join(input_folder, filename), 'r', encoding='utf-8') as f:
#             html_text = f.read()

#         # Split the HTML text into smaller chunks
#         chunks = [html_text[i:i+max_len] for i in range(0, len(html_text), max_len)]

#         # Translate each chunk separately and save to a new HTML file
#         translated_text = ''
#         for chunk in chunks:
#             translated_chunk = GoogleTranslator(source='auto', target='hi').translate(chunk)
#             translated_text += translated_chunk

#         # Save the translated HTML file to the output folder
#         output_file = os.path.join(output_folder, filename)
#         with open(output_file, 'w', encoding='utf-8') as f:
#             f.write(translated_text)





# from googletrans import Translator
# from bs4 import BeautifulSoup as bs

# html = open('index.html').read()
# soup = bs(html,'html.parser')
# translator = Translator()
# text_elements = [element for element in soup.find_all(string=True) if element.parent.name not in ['script', 'style']]

# for element in text_elements:
#     text = element.get_text(strip=True)
#     if not text:
#         continue
#     try:
#         translated_text = translator.translate(text, dest='hi')
#         element.replace_with(translated_text)
#     except Exception as e:
#         print(f"Error translating text: {text}")
#         print(f"Translation error message: {e}")
#         print(f"Translation type: {type(translated_text)}")
#         print(f"Translation result: {translated_text}")
# with open('index_hindi.html', 'w',encoding='utf-8') as f:
#     f.write(str(soup))

import os
import re
import json

from deep_translator import GoogleTranslator

cache_dict = {
    "BIM":"BIM",
    "edX":"edX",
    "CME":"CME",
    "STEM":"STEM",
    "ESL":"ESL",
    "GIS":"GIS",
    "CAD":"CAD",
}

GT = GoogleTranslator(target='hi')

def my_strip(words):
    if '\n' in words:
        words = words.replace('\n', ' ')
        words = words.replace('      ', ' ')
        words = words.replace('     ', ' ')
        words = words.replace('    ', ' ')
        words = words.replace('   ', ' ')
        words = words.replace('  ', ' ')

        words = words.replace('&shy;', '')
        words = words.replace('&amp;', '&')
        words = words.replace('&#039;', '\'')
        words = words.replace('&#8217;', '\'')
        
    return words

def replace(match):
    words = match.group()[1:-1].strip()
    
    if words == '':
        return match.group()
    
    if words in cache_dict.keys():
        if cache_dict[words] == '-----':
            return match.group()
        return cache_dict[words]
    
    if '&&' not in words and len(words) != 0:
        words = my_strip(words)
        print('-'*30)
        print(words,'->')
        try:
            trs = GT.translate(words)
            print(trs)
            trs = '>{0}<'.format(trs)

            cache_dict[words] = trs
            return trs
        except:
            print(f'ERR: translating {words}')
            cache_dict[words] = '-----'
            return match.group()
    else:
        cache_dict[words] = '-----'
        return match.group()

if __name__ == "__main__":
    with open('dict.json','r') as f:
        data = f.read()
    cache_dict = json.loads(data)
    
    for root,dirs,files in os.walk('.'):
        for file in files:
            path = os.path.join(root,file)
            if '.html' not in path:
                continue
            with open(path,"r", encoding="utf-8") as fp:
                html = fp.read()
                print(path + ': ' + str(len(html)))
                pattern = re.compile('>([Ááéíóñúçãa-zA-Z0-9\-\+/~:\:=“”‘!’\(\)%#\?\.\$ \'\"\n,…—`®•●→_|&amp;|&shy;|&nbsp;]+?)<', re.S)
                html2= re.sub(pattern, replace, html)
            with open(path,"w",encoding='utf-8') as fp:
                fp.write(html2)
    data = json.dumps(cache_dict)
    with open('dict.json','w') as f:
        f.write(data)