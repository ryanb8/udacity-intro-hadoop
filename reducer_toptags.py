#!/usr/bin/python
"""
Project:        final_project
File:           reducer_toptags.py
Author:         Ryan Boyer
Email:          bcr5af@virginia.edu

Description:    Reducer to identify top 10 tags

Takes tag data in the format of:
key: tag

Counts number of tags and returns top 10 list

Changelog:      Initial Version 2017 01 31
"""

import sys
import csv


def find_pos(weight, weight_list):
    """
    Finds the postion that a value of weight "weight" would fall in the
    weight_list, where weight_list is sorted by smallest to largest.

    Newer inputs win in ties.

    Return: postion (0 to len(weight_list)-1) or -1 if not in list.
    """
    bool_list = [weight >= x for x in weight_list]
    pos = bool_list.count(True) - 1
    return pos


def adjust_top10(value, pos, weight, top10, top10weights):
    """
    Adjusts top10 list in ascending order, by inserting a new item in
    appropriate place and adjusting others appropriately

    inputs:
        value: the value that is stored in the list
        pos: the position (an integer 0-10) that the new value should go
        weight: the weight tied to this value
        top10: current top10 (as list)
        top10weights: current top10weights
    """
    # Create new top10 to be adjusted
    newtop10 = top10
    newtop10weights = top10weights

    # Keep higher ones, shift lower ones left one
    newtop10[0:pos] = top10[1:pos + 1]
    newtop10weights[0:pos] = top10weights[1:pos + 1]

    # add new ones
    newtop10[pos] = value
    newtop10weights[pos] = weight
    return (newtop10, newtop10weights)


def main():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t',
                        quotechar='"', quoting=csv.QUOTE_ALL)

    # parameters
    cur_tag = None
    cur_tag_count = 0

    # holders
    top10 = [None for x in range(10)]  # holds tags
    top10w = [0 for x in range(10)]    # holds counts

    for line in reader:
        this_tag = line[0]

        if not (cur_tag is None) and this_tag != cur_tag:
            this_pos = find_pos(cur_tag_count, top10w)
            if this_pos != -1:
                adjust_top10(cur_tag, this_pos, cur_tag_count, top10, top10w)

            # reset params
            cur_tag_count = 0

        # Set and Update
        cur_tag = this_tag
        cur_tag_count += 1

    # Sort and Print List
    for i in range(10):
        writer.writerow([top10[i], top10w[i]])


if __name__ == "__main__":
    main()
