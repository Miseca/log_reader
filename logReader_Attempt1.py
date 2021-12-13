# Program to read a log file and return a report
# on unique ips, top 3 urls, top 3 ips


#   First attempt
import sys

if len(sys.argv) == 2:
    print(sys.argv)
else:
    print("No file path specified")
    exit()

try:
    f = open(sys.argv[1])
except:
    print("File not accessible")
    exit()

uniqueIps = []
allIps = []
allUrls = []

with open('../programming-task-example-data_(1).log') as log:
    for line in log:
        #run Checks
        tempIp = line.split(' ')
        if tempIp[0] not in uniqueIps:
            uniqueIps.append(tempIp[0])
        allIps.append(tempIp[0])

        tempLine = line.split('"')
        #run Checks
        tempUrl = tempLine[1].split(' ')
        #run checks
        
        allUrls.append(tempUrl[1])


print(len(uniqueIps))
print(allIps)
print(allUrls)




# print(sys.argv[1])

# dummy = {
#     "ipexample": 1
# }

# dummy[tempId[0]] = dummy[tempId[0]] + 1



try:
    logPath = sys.argv[1]
except:
    print("there was an error")




my_dict = {"A":3,"B":4,"H":1,"K":8,"T":0}
my_keys = sorted(my_dict, key=my_dict.get, reverse=True)[0:3]
# where `my_keys` holds the value:
#     ['K', 'B', 'A']