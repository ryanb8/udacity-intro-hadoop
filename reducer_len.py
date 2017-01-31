#!/usr/bin/python
"""
Project:        final_project
File:           reducer_len.py
Author:         Ryan Boyer
Email:          bcr5af@virginia.edu

Description:     Reducer to compare post length with average repsone length

Takes mapper input in form of:
    key: parentid (or id if self is parent)
    value: Q/A \t len(body)
Reduces to :
    Parentid    BodyLen avgResponseLength

Changelog:      Initial Version 2017 01 31
"""

import sys
import csv


def main():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t',
                        quotechar='"', quoting=csv.QUOTE_ALL)

    # parameters
    cur_parent = None
    cur_parent_len = 0
    cur_response_avg = 0.0
    cur_response_count = 0

    for line in reader:
        this_par = line[0]
        this_type = line[1]
        this_len = int(float(line[2]))

        if not (cur_parent is None) and this_par != cur_parent:
            cur_response_avg = cur_response_avg/cur_response_count
            writer.writerow([cur_parent, cur_parent_len, cur_response_avg])

            # reset em
            cur_parent_len = 0
            cur_response_avg = 0.0
            cur_response_count = 0

        # Set and Update
        cur_parent = this_par
        if this_type == "Q":
            cur_parent_len = this_len
        else:
            cur_response_avg += this_len
            cur_response_count += 1

    # Calc & Print last one
    if not (cur_parent is None):
        cur_response_avg = cur_response_avg / cur_response_count
        writer.writerow([cur_parent, cur_parent_len, cur_response_avg])


if __name__ == "__main__":
    main()
