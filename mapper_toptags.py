#!/usr/bin/python
"""
Project:        final_project
File:           mapper_toptags.py
Author:         Ryan Boyer
Email:          bcr5af@virginia.edu

Description:    Mapper to identify top 10 tags

Takes post data and maps to:
key: tag

Only tags from posts that are "questions" are considered and each is given
its own line.

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
    tag_val = 2
    node_type_val = 5

    # Skip header
    next(reader)

    for line in reader:
        if len(line) == 19:  # validate data
            these_tags = line[tag_val].split()
            this_node_type = line[node_type_val]

            if this_node_type.lower() == 'question':
                # top level node
                for tag in these_tags:
                    writer.writerow([tag])


if __name__ == "__main__":
    main()
