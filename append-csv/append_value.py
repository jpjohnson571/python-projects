'''
Created on Dec 28, 2016

@author: jpjohnson
'''

import sys
import csv


def main(input_file, column, out_file):
    infile = open(input_file, "rb")
    reader = csv.reader(infile)
    outfile = open(out_file, 'wb')
    writer = csv.writer(outfile)
    return(append_csv(reader, writer, column))


def append_csv(read, write, column):
    for row in read:
        if int(read.line_num) == 1:
            write.writerow(row)
        else:
            row[int(column)-1] = 'https://spscommerce.atlassian.net/browse/' + row[int(column)-1]
            write.writerow(row)
    return write


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
