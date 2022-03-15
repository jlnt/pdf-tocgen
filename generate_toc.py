#!/usr/bin/env python3
#
# pylint: disable=missing-docstring
#
# Generates PDF bookmarks from a text file with titles and page numbers
#
# Author: Julien Tinnes

import getopt
import sys


def output_bookmark(name, page, level, offset):
    print("BookmarkBegin")
    print("BookmarkTitle: " + name)
    print("BookmarkLevel: " + str(level))
    print("BookmarkPageNumber: " + str(page + offset))
    print("")


def print_toc(names, pages, offset):
    output_bookmark(names[0], pages[0], 1, offset)
    for i in range(1, len(names)):
        output_bookmark(names[i], pages[i], 2, offset)


def open_and_parse(filename, offset):
    with open(filename, 'r') as toc_input:

        section_names = list()
        section_pages = list()
        parsing_page_numbers = False

        for line in toc_input:
            line = line.strip()
            if not line:
                continue

            if line.isnumeric():
                section_pages.append(int(line))
                parsing_page_numbers = True
            else:
                assert not parsing_page_numbers
                section_names.append(line)

            assert len(section_names) >= len(section_pages)

            if len(section_names) == len(section_pages):
                print_toc(section_names, section_pages, offset)
                section_names = list()
                section_pages = list()
                parsing_page_numbers = False


def usage():
    print("Usage: " + sys.argv[0] + " -f <filename> -o <offset>")


def parse_command_line():
    filename = ""
    offset = -1
    try:
        opts, _ = getopt.getopt(sys.argv[1:], 'f:o:', ['filename', 'offset'])

    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(1)

    for o, a in opts:
        if o in ('-f', '--filename'):
            filename = a
        elif o in ('-o', '--offset'):
            offset = int(a)
        else:
            usage()
            sys.exit()

    if not filename or offset < 0:
        usage()
        sys.exit(1)

    return filename, offset


def main():
    filename, offset = parse_command_line()
    open_and_parse(filename, offset)


if __name__ == '__main__':
    main()
