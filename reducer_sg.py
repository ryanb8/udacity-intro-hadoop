#!/usr/bin/python
"""
Project:        final_project
File:           reducer_sg.py
Author:         Ryan Boyer
Email:          bcr5af@virginia.edu

Description:    Reducer to find studnets who commonly communicate

Takes input data of the form
    key: parentid (or id if self is parent)
    value: student id
Returns
    postid [auth1, auth2, ...]

Changelog:      Initial Version 2017 01 31
"""

import sys
import csv


def main():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t',
                        quotechar='"', quoting=csv.QUOTE_ALL)

    # parameters
    cur_post = None
    cur_ids = []

    for line in reader:
        this_post = line[0]
        this_auth = line[1]

        if not (cur_post is None) and cur_post != this_post:
            writer.writerow([cur_post, cur_ids])
            cur_ids = []

        # Set and Update
        cur_post = this_post
        cur_ids.append(this_auth)

    # Calc & Print last one
    if not (cur_post is None):
        writer.writerow([cur_post, cur_ids])


if __name__ == "__main__":
    main()
