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


url_Dict = {}
ip_Dict = {}

def ip_Logger(line):
    #Checks needed
    tempLine = line.split(' ')
    if tempLine[0] not in ip_Dict:
        ip_Dict[tempLine[0]] = 1
    else:
        ip_Dict[tempLine[0]] = ip_Dict[tempLine[0]] + 1


def url_Logger(line):
    tempLine = line.split('"')
    tempUrl = tempLine[1].split(' ')
    #print(tempUrl)
    if tempUrl[1] not in url_Dict:
        url_Dict[tempUrl[1]] = 1
    else:
        url_Dict[tempUrl[1]] = url_Dict[tempUrl[1]] + 1


with open(sys.argv[1]) as log:
    #
    #
    for line in log:
        url_Logger(line)
        ip_Logger(line)

def dict_Sorter(my_dict):
    my_keys = sorted(my_dict, key = my_dict.get, reverse = True)[0:3]
    
    return {key: my_dict[key] for key in my_keys}
    

print("Total number of unique ips: " + str(len(ip_Dict)))
print(dict_Sorter(url_Dict))
print(dict_Sorter(ip_Dict))

