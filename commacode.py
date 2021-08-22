#! /usr/bin/env python3

cats = ['Bruce', 'Chewie', 'Salem', 'Dinger']

def display_list(list):
    new_list = []
    for items in list[:-1]:
        new_list.append(items)
    print(', '.join(new_list) + ',' + ' and ' + list[-1])
display_list(cats)

