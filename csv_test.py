"""
This file produce csv data, valid according to csv standard, but not easily
parsable without a well coded csv parser.

"""
import os
import csv

FILENAME = 'data.csv'
DELIMITER = ','
DEFAULT_DATA = [
    ['a', 'b', """c
     42,23,7
     60,,"""],
    ['12,00',3,2],
]


def data_from_csv_parser(filename=FILENAME, delimiter=DELIMITER):
    """Parse the data in given csv file with help of the csv standard module"""
    with open(filename) as fd:
        reader = csv.reader(fd, delimiter=delimiter)
        return [line for line in reader]

def data_from_dumb_parser(filename=FILENAME, delimiter=DELIMITER):
    """Parse dumbly the data in given csv file"""
    with open(filename) as fd:
        return [line.split(delimiter) for line in fd]

def create_csv(data=DEFAULT_DATA, delimiter=DELIMITER, filename=FILENAME):
    """Put data in csv file"""
    with open(filename, 'w', newline='') as fd:
        writer = csv.writer(fd, delimiter=delimiter)
        for line in data:
            writer.writerow(line)

def prettified_data(data, line_prefix='\t'):
    """Return the given data, formatted as string"""
    data_prefix = '\n\t'+line_prefix
    return data_prefix + data_prefix.join(str(l) for l in data)

def stats_on_data(data, line_prefix='\t'):
    """Return stats on given data"""
    yield line_prefix + 'Lines size: ' + str(tuple(len(line) for line in data))
    yield line_prefix + 'Nb line: ' + str(len(data))
    yield line_prefix + 'Data: ' + prettified_data(data, line_prefix)


if __name__ == '__main__':
    if os.path.exists(FILENAME):
        # print information about parsed data for each parser
        print('Follows the data in the csv file:')
        print('\n'.join(stats_on_data(DEFAULT_DATA)), '\n')
        print('Follows data retrieved by each parser:\n')
        parsers = (data_from_dumb_parser, data_from_csv_parser)
        for idx, func in enumerate(parsers, start=1):
            print(str(idx) + '. Parser ' + func.__name__ + ' (' + func.__doc__ + ')')
            data = func()
            print('\n'.join(stats_on_data(data)))
            print()
    else:  # the file does'nt exists
        create_csv()
