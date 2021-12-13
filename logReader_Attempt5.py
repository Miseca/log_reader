#
#
#
#
#

import sys


#
def ip_grabber(line, ip_dict):
    tempLine = line.split(' ')
    print(len(tempLine))
    tempIp = tempLine[0]
    #print(tempLine)
    
    #Check that makes sure the first character of the ip is a number and if it fails to return nothing
    if tempIp[0].isdigit():    
        if tempIp not in ip_dict:
            #print({tempIp : 1})
            return {tempIp: 1}
        else:
            return {tempIp: ip_dict[tempIp] + 1}

#
def url_grabber(line, url_dict):
    tempLine = line.split(' ')
    tempUrl = tempLine[6]
    #Check to make sure the function returns an appropriate url and if it fails to return nothing
    if tempUrl[0] == '/' or 'h':
        if tempUrl not in url_dict:
            return {tempUrl: 1}
        else:
            return {tempUrl: url_dict[tempUrl] + 1}
    #else:
        #error

#
def dict_sorter(my_dict):
    my_keys = sorted(my_dict, key = my_dict.get, reverse = True)[0:3]
    
    return {key: my_dict[key] for key in my_keys}
    
def log_printer(ip_dict, url_dict):
    print("Total number of unique ips: " + str(len(ip_dict)))
    print("The top 3 active ip addresses are: " + str(dict_sorter(ip_dict)))
    print("The top 3 most visited urls were: " + str(dict_sorter(url_dict)))

def main():
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


    with open(sys.argv[1]) as log:
        ip_dict = {}
        url_dict = {}
        #finish that
        error_dict = {}
        for line in log:
            ip_dict.update(ip_grabber(line, ip_dict))
            url_dict.update(url_grabber(line, url_dict))
        
        log_printer(ip_dict, url_dict)

if __name__ == "__main__":
    main()
