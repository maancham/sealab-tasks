import os
from os import listdir
from os.path import isfile, join


dir_name = r'test'
file_list = list()
for (dirpath, dirnames, filenames) in os.walk(dir_name):
    file_list += [os.path.join(dirpath, file) for file in filenames]
    
    
# Printing all file names   
for item in file_list:
    print(item)
    
        
        
        