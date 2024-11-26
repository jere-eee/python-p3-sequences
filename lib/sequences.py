#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    current_list = [0, 1]
    
    for n in range(2, length):
        new_n = current_list[-1] + current_list[-2]
        current_list.append(new_n)
        
    print(current_list)