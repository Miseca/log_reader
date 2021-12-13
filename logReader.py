# logReader writted by Sean Selemidis
#
# logReader has the following features:
# outputs: 
#   the total number of unique ips
#   the top 3 most active ip addresses
#   the top 3 most visited urls
#   the number of lines that caught a error
#   a error file with the invalid lines
# There are a number of checks included to
# validate whether the line passed follows
# the correct formatting required for the program

import sys


def line_splitter(line):
    """
        Function used to split each line that is passed through from the log
    """
    line_split_one = line.split("\"-\"")
    # Check used to make sure there are 2 elements in the list and whether
    # the 2nd element is contained within quotation marks
    if len(line_split_one) != 2 or line_split_one[1][1] != "\"" or line_split_one[1][-2] != "\"":
        return "Invalid_Line"

    line_split_two = line_split_one[0].split(" ")
    # Check used to make sure that after the second split there are 11 elements in the list
    if len(line_split_two) != 11:
        return "Invalid_Line"
    return line_split_two


def ip_grabber(ip_string, ip_dict):
    """
        Function that takes the ip component from the split line and
        checks whether it is unique or a repeat and returns a key:value pair
    """
    # Check to make sure the characters of ip_string consist of numbers and periods only
    for character in ip_string:
        if not character.isdigit() and character != '.':
            return "Invalid_Line"

    if ip_string not in ip_dict:
        return {ip_string: 1}
    return {ip_string: ip_dict[ip_string] + 1}


def url_grabber(url_string, url_dict):
    """
        Function that takes the url component from the split line and checks
        whether it is unique or a repeat and returns a key:value pair
    """
    # Check to make sure the function returns an appropriate url
    # and if it fails to return a string used to catch the faulty log
    if url_string[0] == '/' or url_string[0] == 'h':
        if url_string not in url_dict:
            return {url_string: 1}
        return {url_string: url_dict[url_string] + 1}
    return "Invalid_Line"


def dict_sorter(my_dict):
    """
        Function to sort the dictionaries for url and ips and that in the
        event of a tie for 3rd place will extend the length of the array to
        include all elements that match the value of 3rd place
    """
    my_keys = sorted(my_dict, key=my_dict.get, reverse=True)
    sorted_dict = {key: my_dict[key] for key in my_keys}
    i = 3
    for element in range(2, len(my_keys) - 1):
        if sorted_dict[my_keys[element]] == sorted_dict[my_keys[element+1]]:
            i = i + 1
        else:
            break
    top_three_dict = my_keys[:i]
    return {key: my_dict[key] for key in top_three_dict}


def log_printer(ip_dict, url_dict, error_list):
    """
        Function used to print out the results of reading the log and
        to export any errors found as a text file
    """
    print("Total number of unique ips: " + str(len(ip_dict)))
    print("The top 3 active ip addresses are: " + str(dict_sorter(ip_dict)))
    print("The top 3 most visited urls were: " + str(dict_sorter(url_dict)))
    print(str(len(error_list)) +
          " lines were flagged and have been exported to errorlog.txt")
    # Lines that have caught an error are being
    # exported as a text file called errorlog.txt
    with open('errorlog.txt', 'w') as f:
        for line in error_list:
            f.write(line)
        f.close()


def main():
    """
        Runs log file and does the main logic
    """
    # Check used to make sure there was a file path specified
    if len(sys.argv) == 2:
        print("Reading " + sys.argv[1])
    else:
        print("No file path specified")
        exit()
    # Check used to make sure the file specified is exists and readable
    try:
        f = open(sys.argv[1])
        f.close()
    except:
        print("File not accessible or does not exist")
        exit()

    # Open file and process it
    with open(sys.argv[1]) as log:
        ip_dict = {}
        url_dict = {}
        error_list = []
        for line in log:

            split_line = line_splitter(line)
            # Check that if line_splitter returns invalid line add it to error_list
            if split_line == "Invalid_Line":
                error_list.append(line)
            else:
                line_ip = ip_grabber(split_line[0], ip_dict)
                line_url = url_grabber(split_line[6], url_dict)
                # Check that if line_ip or line_url returns invalid line add it to error_list
                if line_ip == "Invalid_Line" or line_url == "Invalid_Line":
                    error_list.append(line)
                else:
                    ip_dict.update(line_ip)
                    url_dict.update(line_url)
        

        log_printer(ip_dict, url_dict, error_list)


if __name__ == "__main__":
    main()
