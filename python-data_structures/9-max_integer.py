#!/usr/bin/python3
def max_integer(my_list=[]):
    maximum = 0
    if len(my_list) == 0:
        return None
    else:
        for i in my_list:
            if my_list[i] > maximum:
                maximum =my_list[i]
        return maximum
