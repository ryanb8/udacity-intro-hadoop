#!/usr/bin/python
"""
Project:        final_project
File:           mapper_sg.py
Author:         Ryan Boyer
Email:          bcr5af@virginia.edu

Description:    Mapper to find students who commonly communicate

Takes post data and maps to:
key: parentid (or id if self is parent)
value: student id

Post data format:
Fields:
    0-5     "id"	"title"	"tagnames"	"author_id"	"body"	"node_type"
    6-10    "parent_id" "abs_parent_id"	"added_at"	"score"	"state_string"
    11-13   "last_edited_id" "last_activity_by_id"	"last_activity_at"
    14-17   "active_revision_id"	"extra" "extra_ref_id"	"extra_count"
    18      "marked"
Has Header

Changelog:      Initial Version 2017 01 31
"""

import sys
import csv


def main():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t',
                        quotechar='"', quoting=csv.QUOTE_ALL)

    # parameters
    id_val = 0
    auth_val = 3
    parent_val = 7

    # Skip header
    next(reader)

    for line in reader:
        if len(line) == 19:  # Node (id = first)
            this_id = line[id_val]
            this_auth = line[auth_val]
            this_parent = line[parent_val]

            if this_parent == '\\N':
                # top level node
                writer.writerow([this_id, this_auth])
            else:
                # answer
                writer.writerow([this_parent, this_auth])


if __name__ == "__main__":
    main()
