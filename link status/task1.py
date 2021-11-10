import os
import re

base_urls = ['https://', 'http://']
  
def clean_urls_list(urls):
    new_urls = [s.replace('},', '').replace('"', '') for s in urls]
    for i in range(len(new_urls)):
        if ("\\" in new_urls[i]):
            new_urls[i] = new_urls[i].split('\\')[0]
        if ('}' in new_urls[i]):
            new_urls[i] = new_urls[i].split('}')[0]

    new_urls = [s for s in new_urls if s not in base_urls]
    return new_urls


dir_name = r'test'
file_list = list()
for (dirpath, dirnames, filenames) in os.walk(dir_name):
    file_list += [os.path.join(dirpath, file) for file in filenames]

for file in file_list:
    with open(file, 'r', encoding="utf8") as target:
        file_text = target.read()
        urls = re.findall(r'(https?://[^\s]+)', file_text)
        print(clean_urls_list(urls))        

        
        