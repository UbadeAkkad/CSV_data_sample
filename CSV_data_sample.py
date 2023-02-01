import csv
import random

def Create_CSV_Sample(filename, outputfile='', delimiter=',', lines = 10, headers=True, randomize=False):

    """
    To create a sample file out of a CSV data file.

    Arguments:
        filename {string} -- CSV file name without the .csv file extension.
        outputfile {string} -- Name of the output sample file, if not assigned the output file will be named "Sample_{filename}"
        delimiter {string} -- Input file used CSV delimiter.
        lines {int} -- Number of rows in the sample file.
        headers {bool} -- Set to true to include original file header in the sample file.
        randomize {bool} -- Set to True to randomize the rows taken from the original file.
    """

    input_file = open(filename + ".csv", 'r', encoding='utf-8')
    reader = csv.reader(input_file, delimiter=delimiter)

    if outputfile == "":
        outputname = "Sample_" + filename + ".csv"
    else:
        outputname = outputfile + ".csv"

    writer = csv.writer(open(outputname, 'w',encoding='utf-8', newline=''), delimiter=delimiter)

    if headers:
        writer.writerow(next(reader))

    if not randomize:
        for i, row in enumerate(reader):
            if i < lines:
                writer.writerow(row)
            else:
                break
    else:
        data_list = list(reader)
        data_rows_len = len(data_list)
        random_list = random.sample(range(data_rows_len), lines)
        for i in random_list:
            writer.writerow(data_list[i])

