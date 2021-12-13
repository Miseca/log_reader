#
#
#
#
#

import sys

if len(sys.argv) == 2:
    print("Reading " + sys.argv[1])
else:
    print("No file path specified")
    exit()

try:
    f = open(sys.argv[1])
except:
    print("File not accessible")
    exit()


def ip_logger(line):
    #Checks needed
    tempLine = line.split(' ')
    print(tempLine)
    if tempLine[0] not in ip_dict:
        ip_dict[tempLine[0]] = 1
    else:
        ip_dict[tempLine[0]] = ip_dict[tempLine[0]] + 1


def url_logger(line):
    tempLine = line.split('"')
    tempUrl = tempLine[1].split(' ')
    #print(tempUrl)
    if tempUrl[1] not in url_dict:
        url_dict[tempUrl[1]] = 1
    else:
        url_dict[tempUrl[1]] = url_dict[tempUrl[1]] + 1

def dict_sorter(my_dict):
    my_keys = sorted(my_dict, key = my_dict.get, reverse = True)[0:3]
    
    return {key: my_dict[key] for key in my_keys}
    
def log_printer(ip_dict, url_dict):
    print("Total number of unique ips: " + str(len(ip_dict)))
    print("The top 3 active ip addresses are: " + str(dict_sorter(ip_dict)))
    print("The top 3 most visited urls were: " + str(dict_sorter(url_dict)))

with open(sys.argv[1]) as log:
    ip_dict = {}
    url_dict = {}
    for line in log:
        url_logger(line)
        ip_logger(line)
    
    # dict_sorter(ip_dict)
    # dict_sorter(url_dict)
    log_printer(ip_dict, url_dict)