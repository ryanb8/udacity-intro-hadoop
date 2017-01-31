#!/usr/local/bin/python3.6
# For some reason, on the virtual machine supplied by Udacity, #!/usr/bin
# and #!/usr/bin/env do not have python executables... --> hard coded locations
"""
Project:        final_project
File:           mapper_activehour.py
Author:         Ryan Boyer
Email:          bcr5af@virginia.edu

Description:    Mapper to find for each student what is the hour during
which the student has posted the most posts.

Takes post data and maps to:
key: authorid
value: post time

Post data format:
Fields:
    0-5     "id"	"title"	"tagnames"	"author_id"	"body"	"node_type"
    6-10    "parent_id" "abs_parent_id"	"added_at"	"score"	"state_string"
    11-13   "last_edited_id" "last_activity_by_id"	"last_activity_at"
    14-17   "active_revision_id"	"extra" "extra_ref_id"	"extra_count"
    18      "marked"
Has Header

Changelog:      Initial Version 2017 01 30
"""

import sys
import csv
import re


def main():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t',
                        quotechar='"', quoting=csv.QUOTE_ALL)

    # parameters
    author_val = 3
    dt_val = 8

    # regex set up
    # e.g datetime string: "2012-02-25 08:11:01.623548+00"
    dt_re = r"([0-9]{4})-([0-9]{2})-([0-9]{2}) ([0-9]{2}):([0-9]{2}):([0-9]{2}.[0-9]{6})\+([0-9]{2})"

    # Skip header
    next(reader)

    for line in reader:
        if len(line) == 19:  # Node (id = first)
            this_auth = [line[author_val]]
            this_time = [re.findall(dt_re, line[dt_val])[0][3]]
            writer.writerow(this_auth + this_time)

if __name__ == "__main__":
    main()
