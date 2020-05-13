# -*- coding: utf-8 -*-
"""
Created on Tue May  5 08:29:37 2020

@author: Joseph
"""

__author__ = "Joe Cox"
__email__ = "jocox@students.columbiabasin.edu"
__date_ = "Spring 2020"
__version__ = "0.0.1"


# LIBRARIES
from datetime import date
import os
import pickle
import json
import subprocess
from difflib import SequenceMatcher

# SET VARIABLES
my_dir = '/Users/Joseph/Downloads/830199374'
my_pickle = my_dir + '/data.pickle'
my_json = my_dir + '/data.json'
port_list = ['192.168.1.1:80', '192.168.1.1:23', '192.168.1.1:22']
nmap_path = '/Users/Joseph/Desktop/nmap-7.70/nmap.exe'
nmap_network = '192.168.1.1'

def create_directory():   
    if(os.path.isdir(my_dir)) == False:
        try:  
            os.mkdir(my_dir)
            print ("INFO: The directory was created:", my_dir) 
        except OSError:  
            print ("ERROR: Failed to create directory:", my_dir)
    else:
        print ("INFO: The directory already exists:", my_dir) 
        
def create_date_string():
    date_str = date.today().strftime("%m%d%y")
    return (date_str)

def write_files(input_data, file_name):
    #write the pickle file
    with open(str(my_dir) + '/' + str(file_name) + '.pickle', 'wb') as fp:
        pickle.dump(input_data, fp)
    fp.close()
    
    # write the json file
    with open(str(my_dir) + '/' + str(file_name) + '.json', 'w') as fp:  
        json.dump(input_data, fp)
    fp.close()
    

def read_files(seq, file_name):
    port_list = []
    
    
    
    # read the pickle file
    with open (str(my_dir) + '/' + str(file_name) + '.pickle' , 'rb') as fp:
        port_list = pickle.load(fp)
    fp.close()
    
    print("pickle:", port_list)
    
    port_list = []
    
    # read the json file
    with open(str(my_dir) + '/' + str(file_name) + '.json' ,'r') as fp:  
        port_list = json.load(fp)
    fp.close()
    
    print("json:", port_list)


def run_nmap():
    nmap_out = subprocess.run([nmap_path, "-T4", nmap_network], capture_output=True)
    nmap_data = nmap_out.stdout.splitlines()
    #nmap_data = 'nmap output'
    return nmap_data


    
create_directory()
input_data = run_nmap()
print(input_data)
file_name = create_date_string()
write_files(input_data, file_name)

import filecmp

path = my_dir
comparison = filecmp.dircmp(path+ '051220.json' ,path+ '051220.pickle')
common_files = ','.join(comparison.common)
left_only_file = ','.join(comparison.left_only)
right_only_file = ','.join(comparison.right_only)
with open(path+'folder_diff.txt' , 'w') as folder_report:
    folder_report.write("common files: "+common_files+ '\n')
    folder_report.write('\n'+"only in json file"+left_only_file+'\n')
    folder_report.write('\n'+"only in pickle file"+right_only_file+'\n')
    




