#!/usr/local/bin/python3.6
# For some reason, on the virtual machine supplied by Udacity, #!/usr/bin
# and #!/usr/bin/env do not have python executables... --> hard coded locations
"""
Project:        final_project
File:           reducer_activehour.py
Author:         Ryan Boyer
Email:          bcr5af@virginia.edu

Description:    reducer to find for each student what is the hour during
which the student has posted the most posts.

input:
key: authorid
value: post time

Returns:
Key: Authorid
Value : Most common hour
NOTE: if there are multiple most common hours, returns all

Changelog:      Initial Version 2017 01 30
"""

import sys
import csv


def main():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t',
                        quotechar='"', quoting=csv.QUOTE_ALL)

    # parameters
    cur_author = None
    hour_counter = [0] * 24

    for line in reader:
        this_auth = line[0]
        this_hour = int(float(line[1]))

        if not (cur_author is None) and this_auth != cur_author:
            # calc max
            max_posts = max(hour_counter)
            max_posts = [i for (i, x) in enumerate(hour_counter) if x ==
                         max_posts]

            # print em
            for i in max_posts:
                writer.writerow([cur_author, max_posts[i]])

            # reset em
            hour_counter = [0] * 24

        # Set and Update
        cur_author = this_auth
        hour_counter[this_hour] += 1

    # Print last one
    for i in max_posts:
        writer.writerow([cur_author, max_posts[i]])


if __name__ == "__main__":
    main()
