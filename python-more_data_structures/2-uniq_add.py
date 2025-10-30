#!/usr/bin/python3
def uniq_add(my_list=[]):
    aset = set(my_list)
    total = 0
    for i in aset:
        total += i
    return total
