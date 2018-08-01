#!/usr/bin/python3
import sys

def mention_subgroup(groups, sender, group_list):
    mentions = ''

    for group in groups:
        group_name = group[:2].upper()

        if group_name not in group_list.keys():
            continue
        
        for user in group_list[group_name]:
            if user in mentions or user == sender:
                continue
            
            mentions += "@{} ".format(user)

    return mentions
