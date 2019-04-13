##################################################################
# FileName: Sandbox/python_test.py
# HeadLine: Akamai Coding Challenge script
# Description:
# To Be Added
##################################################################

import __init__
import sys


from Sandbox.functions import *

SUFFIX = ".txt"
DOMAIN_NAME = "example.com"

###################### script input validation #######################################

# if there is wrong number of arguments
if len(sys.argv) != 3:
    raise Exception("This script should get 2 arguments, but you tried to run it with {}".format((len(sys.argv) - 1)))

# if the arguments aren't text files
if (sys.argv[1].endswith(SUFFIX) or sys.argv[2].endswith(SUFFIX)) is False:
    raise Exception("This script arguments should be text file")


iFile = sys.argv[1]
oFile = sys.argv[2]

file_parser = File_Parser()

file_content = file_parser.f_read(iFile)

parsed_content = ""

# if the file isn't empty
if file_content != "":
    for line in file_content.split("\n"):
        temp = line.split()
        if file_parser.is_valid_ip_address(temp[3]):  # if the ip address is valid
            parsed_content += "{0} {1} {1}.{2}\n".format(temp[3], temp[0], DOMAIN_NAME)

file_parser.f_write(parsed_content, oFile)

# file_parser.f_write(file_content, oFile)



