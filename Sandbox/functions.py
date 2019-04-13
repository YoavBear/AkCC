##################################################################
# FileName: Functions/functions.py
# HeadLine: Akamai Coding Challenge functions
# Description:
# To Be Added
##################################################################

# Python Imports
import logging
from curses.ascii import isdigit

SUFFIX = ".txt"
DOMAIN_NAME = "example.com"


class File_Parser:
    """
    Text Files Parser
    """

    def f_read(self, file_name):
        """
        Reads file_name content and return it as a string
        :param file_name:
        :return: file_name content as a string
        """
        if file_name.endswith(SUFFIX) is False:
            raise Exception("wrong file format! a .txt file required here")
        try:
            with open(file_name, 'r') as file:
                file_content = file.read()
        except IOError:
            print("Could not open {}".format(file_name))
        return file_content


    def f_write(self, data, file_name):
        """
        writes the data as a string to the file_name
        :param data:
        :param file_name:
        :return:
        """
        if type(data) is not str:
            raise Exception("wrong input! f_write should accept str while the input is {}".format(type(data)))
        if file_name.endswith(SUFFIX) is False:
            raise Exception("wrong file format! a .txt file required here")

        try:
            with open(file_name, 'w') as file:
                file.write(data)
        except IOError:
            print("Could not open {}".format(file_name))

    ### f_write with content restructure
    # def f_write(self, data, file_name):
    #     """
    #     writes the data as a string to the file_name
    #     :param data:
    #     :param file_name:
    #     :return:
    #     """
    #     if type(data) is not str:
    #         raise Exception("wrong input! f_write should accept str while the input is {}".format(type(data)))
    #     if file_name.endswith(SUFFIX) is False:
    #         raise Exception("wrong file format! a .txt file required here")
    #
    #     try:
    #         with open(file_name, 'w') as file:
    #             for line in data.split("\n"):
    #                 temp = line.split()
    #                 file.write("{0} {1} {1}.{2}\n".format(temp[3], temp[0], DOMAIN_NAME))
    #     except IOError:
    #         print("Could not open {}".format(file_name))

    def is_valid_ip_address(self, address):

        for word in address.split("."):
            if word.isdigit() is False:
                return False

        if len(address.split(".")) != 4:
            return False
        else:
            return True









